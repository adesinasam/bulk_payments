from __future__ import unicode_literals
from frappe import _
import frappe


def get_data():
	config = [
		
		{
			"label": _("General Ledger"),
			"items": [
				{
					"type": "doctype",
					"name": "Bulk Payments Entry",
					"description": _("Capture Bulk Payments"),
            		"link": "List/Bulk Payments Entry/Link"
				}
			]
		},
		{
			"label": _("Reports"),
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Bulk Payments Register",
					"doctype": "Bulk Payments Entry",
            		"link": "List/Bulk Payments Entry/Report/Bulk Payments Register"
					
				}
			]
		}

	]
	return config
