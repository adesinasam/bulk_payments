import frappe
from frappe import _
from frappe import utils


def setup(bulk_payments_entry, method):
    # add payments up and set the total field
    # add default project and cost center to bulk_payments items

    make_journal_entry(bulk_payments_entry)


@frappe.whitelist()
def initialise_journal_entry(bulk_payments_entry_name):
    # make JE from javascript form Make JE button

    make_journal_entry(
        frappe.get_doc('Bulk Payments Entry', bulk_payments_entry_name)
    )


def make_journal_entry(bulk_payments_entry):
        pr_name = frappe.db.get_value("Journal Entry",{"bill_no": bulk_payments_entry.name}, "name")
        
        pr = frappe.get_doc("Journal Entry", pr_name)
        pr.cancel()

   
