import frappe
from frappe import _
from frappe import utils


def setup(bulk_payments_entry, method):
    # add payments up and set the total field
    # add default project and cost center to bulk_payments items

    total = 0
    count = 0
    bulk_payments_items = []

    
    for detail in bulk_payments_entry.payments:
        total += float(detail.amount)        
        count += 1
        
        if not detail.project and bulk_payments_entry.default_project:
            detail.project = bulk_payments_entry.default_project
        
        if not detail.cost_center and bulk_payments_entry.default_cost_center:
            detail.cost_center = bulk_payments_entry.default_cost_center

        bulk_payments_items.append(detail)

    bulk_payments_entry.payments = bulk_payments_items

    bulk_payments_entry.total = total
    bulk_payments_entry.quantity = count

    make_journal_entry(bulk_payments_entry)

    


@frappe.whitelist()
def initialise_journal_entry(bulk_payments_entry_name):
    # make JE from javascript form Make JE button

    make_journal_entry(
        frappe.get_doc('Bulk Payments Entry', bulk_payments_entry_name)
    )


def make_journal_entry(bulk_payments_entry):

    if bulk_payments_entry.status == "Approved":         

        # check for duplicates
        
        if frappe.db.exists({'doctype': 'Journal Entry', 'bill_no': bulk_payments_entry.name}):
            frappe.throw(
                title="Error",
                msg="Journal Entry {} already exists.".format(bulk_payments_entry.name)
            )


        # Preparing the JE: convert bulk_payments_entry details into je account details

        accounts = []

        for detail in bulk_payments_entry.payments:            

            accounts.append({  
                'debit_in_account_currency': float(detail.amount),
                'user_remark': str(detail.description),
                'account': detail.bulk_payments_account,
                'project': detail.project,
                'cost_center': detail.cost_center
            })

        # finally add the payment account detail

        pay_account = ""

        if (bulk_payments_entry.mode_of_payment != "Cash" and (not 
            bulk_payments_entry.payment_reference or not bulk_payments_entry.clearance_date)):
            frappe.throw(
                title="Enter Payment Reference",
                msg="Payment Reference and Date are Required for all non-cash payments."
            )
#         else:
#             bulk_payments_entry.clearance_date = ""
#             bulk_payments_entry.payment_reference = ""


        pay_account = frappe.db.get_value('Mode of Payment Account', {'parent' : bulk_payments_entry.mode_of_payment, 'company' : bulk_payments_entry.company}, 'default_account')
        


        if not pay_account or pay_account == "":
            frappe.throw(
                title="Error",
                msg="The selected Mode of Payment has no linked account."
            )

        accounts.append({  
            'credit_in_account_currency': float(bulk_payments_entry.total),
            'user_remark': str(detail.description),
            'account': pay_account
        })

        # create the journal entry
        je = frappe.get_doc({
            'title': bulk_payments_entry.name,
            'doctype': 'Journal Entry',
            'voucher_type': 'Journal Entry',
            'posting_date': bulk_payments_entry.posting_date,
            'company': bulk_payments_entry.company,
            'accounts': accounts,
            'user_remark': bulk_payments_entry.remarks,
            'mode_of_payment': bulk_payments_entry.mode_of_payment,
            'cheque_date': bulk_payments_entry.clearance_date,
            'reference_date': bulk_payments_entry.clearance_date,
            'cheque_no': bulk_payments_entry.payment_reference,
            'pay_to_recd_from': bulk_payments_entry.payment_to,
            'bill_no': bulk_payments_entry.name
        })

        user = frappe.get_doc("User", frappe.session.user)

        full_name = str(user.first_name) + ' ' + str(user.last_name)
        bulk_payments_entry.db_set('approved_by', full_name)
        

        je.insert()
        je.submit()
    
    elif bulk_payments_entry.status == "Cancelled":

        pr_name = frappe.db.get_value("Journal Entry",{"bill_no": bulk_payments_entry.name}, "name")
        
        pr = frappe.get_doc("Journal Entry", pr_name)
        pr.cancel()
  

   
