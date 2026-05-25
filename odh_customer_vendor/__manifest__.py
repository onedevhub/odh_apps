# -*- coding: utf-8 -*-
# Part of OneDevHub.

{
    "name": "Customer Supplier Option",
    'version': '17.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'Restores the classic separate Customer and Vendor checkboxes to Odoo 13 contacts. Easily distinguish, filter, and manage partners just like in previous Odoo versions for improved workflow clarity',
    'description': """
        Restores the classic separate Customer and Vendor checkboxes to Odoo 13 contacts. Easily distinguish, filter, and manage partners just like in previous Odoo versions for improved workflow clarity
    """,
    'author': 'OneDevHub',
    'website': 'https://onedevhub.in',
    'license': 'OPL-1',
    'depends': [
        "sale_management",
        "purchase",
    ],
    "data": [
        "views/res_partner_views.xml",
        "views/purchase_views.xml",
        "views/sale_order_views.xml",
    ],
    "images": ["static/description/banner_image.jpg"],
    'installable': True,
    'application': True,
    'auto_install': False,
}