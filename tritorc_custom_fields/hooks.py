from . import __version__ as app_version

app_name = "tritorc_custom_fields"
app_title = "Tritorc Custom Fields"
app_publisher = "Firsterp"
app_description = "Custom fields for Tritorc India"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "support@fristerp.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/tritorc_custom_fields/css/tritorc_custom_fields.css"
# app_include_js = "/assets/tritorc_custom_fields/js/tritorc_custom_fields.js"

# include js, css files in header of web template
# web_include_css = "/assets/tritorc_custom_fields/css/tritorc_custom_fields.css"
# web_include_js = "/assets/tritorc_custom_fields/js/tritorc_custom_fields.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "tritorc_custom_fields/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

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

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "tritorc_custom_fields.install.before_install"
# after_install = "tritorc_custom_fields.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "tritorc_custom_fields.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
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
# 		"tritorc_custom_fields.tasks.all"
# 	],
# 	"daily": [
# 		"tritorc_custom_fields.tasks.daily"
# 	],
# 	"hourly": [
# 		"tritorc_custom_fields.tasks.hourly"
# 	],
# 	"weekly": [
# 		"tritorc_custom_fields.tasks.weekly"
# 	]
# 	"monthly": [
# 		"tritorc_custom_fields.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "tritorc_custom_fields.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "tritorc_custom_fields.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "tritorc_custom_fields.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"tritorc_custom_fields.auth.validate"
# ]

