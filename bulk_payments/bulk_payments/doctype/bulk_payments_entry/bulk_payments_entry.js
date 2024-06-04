// Copyright (c) 2020, Bantoo and contributors
// For license information, please see license.txt

frappe.provide("bulk_payments_entry.bulk_payments_entry");

function update_totals(frm, cdt, cdn){
	var items = locals[cdt][cdn];
    var total = 0;
    var quantity = 0;
    frm.doc.payments.forEach(
        function(items) { 
            total += items.amount;
            quantity +=1;
        });
    frm.set_value("total", total);
    refresh_field("total");
    frm.set_value("quantity", quantity);
    refresh_field("quantity");
}

frappe.ui.form.on('Bulk Payments Entry Item', {
	amount: function(frm, cdt, cdn) {
        update_totals(frm, cdt, cdn);
	},
	payments_remove: function(frm, cdt, cdn){
        update_totals(frm, cdt, cdn);
	},
    payments_add: function(frm, cdt, cdn){
        var d = locals[cdt][cdn];
        
        if((d.cost_center === "" || typeof d.cost_center == 'undefined')) { 

            if (cur_frm.doc.default_cost_center != "" || typeof cur_frm.doc.default_cost_center != 'undefined') {
                
                d.cost_center = cur_frm.doc.default_cost_center; 
                cur_frm.refresh_field("payments");
            }
        }
	}
	
});


frappe.ui.form.on('Bulk Payments Entry', {
    before_save: function(frm) { 

        $.each(frm.doc.payments, function(i, d) { 
            let label = "";
            
            if((d.cost_center === "" || typeof d.cost_center == 'undefined')) { 
                
                if (cur_frm.doc.default_cost_center === "" || typeof cur_frm.doc.default_cost_center == 'undefined') {
                    frappe.validated = false;
                    frappe.msgprint("Set a Default Cost Center or specify the Cost Center for payments <strong>number " 
                                    + (i + 1) + "</strong>.");
                    return false;
                }
                else {
                    d.cost_center = cur_frm.doc.default_cost_center; 
                }
            }
        }); 
        
    },
    refresh(frm) {
        //update total and qty when an item is added
	},
	onload(frm) {
	    //console.log("hello");

		frm.set_query("bulk_payments_account", 'payments', () => {
			return {
				filters: [
					["Account", "company", "=", frm.doc.company],
					["Account", "root_type", "=", "Asset"],
					["Account", "account_type", "=", "Receivable"],
                    ["Account", "is_group", "=", "0"]
				]
			}
		});
		frm.set_query("party_type", 'payments', () => {
			return {
				filters: [
				    ["Doctype", "name", "in", ["Customer"]]
				]
			}
		});
		frm.set_query("party", 'payments', () => {
			return {
				filters: [
				    ["Customer", "disabled", "=", "0"]
				]
			}
		});
		frm.set_query("cost_center", 'payments', () => {
			return {	
				filters: [
					["Cost Center", "company", "=", frm.doc.company],
					["Cost Center", "is_group", "=", "0"]
				]
			}
		});
		frm.set_query("default_cost_center", () => {
			return {
				filters: [
					["Cost Center", "company", "=", frm.doc.company],
					["Cost Center", "is_group", "=", "0"]
				]
			}
		});
		
	}

});