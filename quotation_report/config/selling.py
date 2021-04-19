from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
            "label": _("Key Reports"),
			"items": [
				{
					"type": "report",
					"name": "Quotation Report",
					"doctype": "Quotation",
					"is_query_report": True
				},
				
            ]
		}
	] 