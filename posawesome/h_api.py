import frappe

@frappe.whitelist()
def generate_salesinvoice_barcode(doc, method):
    if not doc.custom_barcode:
        doc.custom_barcode = doc.name
