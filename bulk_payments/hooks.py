# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "bulk_payments"
app_title = "Bulk Payments"
app_publisher = "Glistercp"
app_description = "Bulk Payments Entry for ERPNext"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "support@glistercp.com.ng"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/bulk_payments/css/bulk_payments.css"
# app_include_js = "/assets/bulk_payments/js/bulk_payments.js"

# include js, css files in header of web template
# web_include_css = "/assets/bulk_payments/css/bulk_payments.css"
# web_include_js = "/assets/bulk_payments/js/bulk_payments.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "bulk_payments.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "bulk_payments.install.before_install"
# after_install = "bulk_payments.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "bulk_payments.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Bulk Payments Entry": {
		"on_submit": "bulk_payments.api.setup",
		"on_cancel": "bulk_payments.apy.setup"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"bulk_payments.tasks.all"
# 	],
# 	"daily": [
# 		"bulk_payments.tasks.daily"
# 	],
# 	"hourly": [
# 		"bulk_payments.tasks.hourly"
# 	],
# 	"weekly": [
# 		"bulk_payments.tasks.weekly"
# 	]
# 	"monthly": [
# 		"bulk_payments.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "bulk_payments.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "bulk_payments.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "bulk_payments.task.get_dashboard_data"
# }


fixtures = ["Workflow", "Workflow State", "Workflow Action Master",
	{
		"dt": "Print Format",
		"filters": [
			[
				"name", "in", [
					"Bulk Payments Entry"
				]
			]
		]

	},
	# {
	# 	"dt": "Custom Field",
	# 	"filters": [
	# 		[
	# 			"name", "in", [
	# 				"Accounts Settings-expense_settings",
	# 				"Accounts Settings-default_mode_of_payment",
	# 				"Accounts Settings-column_break_16",
	# 				"Accounts Settings-notify_all_approvers",
	# 				"Accounts Settings-create_journals_entries_automatically"
	# 			]
	# 		]
	# 	]
	# },
	{
		"dt": "Notification",
			"filters": [
[
                                        "name", "in", [
                                                "Bulk Payments Entry",
                                        ]
                                ]
			]
	},
	{
		"dt": "Report",
			"filters": [
				[
					"ref_doctype", "in", [
						"Bulk Payments Entry",
						"Journal Entry"
					]
				]
			]
	}
]
