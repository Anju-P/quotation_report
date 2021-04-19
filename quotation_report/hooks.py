# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "quotation_report"
app_title = "Quotation Report"
app_publisher = "Momscode Technologies Pvt.Ltd"
app_description = "to generate quotation values"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "anju.p@momscode.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/quotation_report/css/quotation_report.css"
# app_include_js = "/assets/quotation_report/js/quotation_report.js"

# include js, css files in header of web template
# web_include_css = "/assets/quotation_report/css/quotation_report.css"
# web_include_js = "/assets/quotation_report/js/quotation_report.js"

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
# get_website_user_home_page = "quotation_report.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "quotation_report.install.before_install"
# after_install = "quotation_report.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "quotation_report.notifications.get_notification_config"

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

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"quotation_report.tasks.all"
# 	],
# 	"daily": [
# 		"quotation_report.tasks.daily"
# 	],
# 	"hourly": [
# 		"quotation_report.tasks.hourly"
# 	],
# 	"weekly": [
# 		"quotation_report.tasks.weekly"
# 	]
# 	"monthly": [
# 		"quotation_report.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "quotation_report.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "quotation_report.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "quotation_report.task.get_dashboard_data"
# }

