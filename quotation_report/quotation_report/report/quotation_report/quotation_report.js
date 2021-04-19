// Copyright (c) 2016, Momscode Technologies Pvt.Ltd and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Quotation Report"] = {
	"filters": [
		{
			fieldname: "quotation",
			label: __("Quotation"),
			fieldtype: "Link",
			options: "Quotation",
			reqd: 1
		},
	]
};