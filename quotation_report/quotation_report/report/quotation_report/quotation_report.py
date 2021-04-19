# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt
 #Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from pprint import pprint

def execute(filters=None):
	data = []
	columns = get_columns()
	get_data(filters, data)
	return columns, data

def get_data(filters, data):
	get_exploded_items(filters.quotation, data)

def get_exploded_items(quotation, data, indent=0):
	exploded_items = frappe.get_list("Quotation Item",
		filters={"parent": quotation},
		fields= ['qty','qty','item_code','short_description','item_name','description','uom','price_list_rate','rate','amount','rate_with_margin_of_stock_items','rate_with_margin_of_activity_items'])

	for item in exploded_items:
		item["indent"] = indent
		data.append({
			'item_code': item.item_code,
			'item_name': item.item_name,
			'indent': indent,
			#'bom': item.bom_no,
			'qty': item.qty,
			'uom': item.uom,
			'short_description': item.short_description,
			'price_list_rate': item.price_list_rate,
			'rate': item.rate,
			'amount': item.amount,
			'rate_with_margin_of_stock_items':item.rate_with_margin_of_stock_items,
			'rate_with_margin_of_activity_items':item.rate_with_margin_of_activity_items,


			})
		if item.bom_no:
			get_exploded_items(item.bom_no, data, indent=indent+1)

def get_columns():
	return [
		{
			"label": "Item Code",
			"fieldtype": "Link",
			"fieldname": "item_code",
			"width": 300,
			"options": "Item"
		},
		{
			"label": "Short Description",
			"fieldtype": "Data",
			"fieldname": "short_description",
			"width": 100
		},
		
		{
			"label": "Qty",
			"fieldtype": "data",
			"fieldname": "qty",
			"width": 100
		},
		{
			"label": "Price List Rate",
			"fieldtype": "Float",
			"fieldname": "price_list_rate",
			"width": 100
		},
		{
			"label": " Rate",
			"fieldtype": "Float",
			"fieldname": "rate",
			"width": 100
		},
		{
			"label": "Total Rate",
			"fieldtype": "Float",
			"fieldname": "amount",
			"width": 100
		},
		{
			"label": "Total Material with Margin",
			"fieldtype": "Float",
			"fieldname": "rate_with_margin_of_stock_items",
			"width": 100
		},
		{
			"label": "Total Activity with Margin",
			"fieldtype": "Float",
			"fieldname": "rate_with_margin_of_activity_items",
			"width": 100
		},
		{
			"label": "Total",
			"fieldtype": "Float",
			"fieldname": "amount",
			"width": 100
		},
		{
			"label": "Material with Margin and Tax",
			"fieldtype": "Float",
			"fieldname": "material_with_margin",
			"width": 100
		},
		{
			"label": "Activity with Margin and Tax",
			"fieldtype": "Float",
			"fieldname": "material_with_margin",
			"width": 100
		},
		{
			"label": "Total Unitprice with Margin & Tax",
			"fieldtype": "Float",
			"fieldname": "rate",
			"width": 100
		},
		{
			"label": "Total Margin & Tax",
			"fieldtype": "Float",
			"fieldname": "amount",
			"width": 100
		},
	]
