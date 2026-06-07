# -*- coding: utf-8 -*-
# Part of OneDevHub.
{
    "name": "Customer Supplier Option",
    'version': '19.0.1.0.0',
    'category': 'Extra Tools',
    'summary': '',
    'description': """
        
    """,
    'author': 'OneDevHub',
    'website': 'https://onedevhub.in',
    'license': 'LGPL-3',
    'depends': [
        "sale_management",
        "purchase",
    ],
    "data": [
        "views/res_partner_views.xml",
        "views/purchase_views.xml",
        "views/sale_order_views.xml",
    ],
     "images": ["static/description/app_img/banner_image.jpg"],
    'installable': True,
    'application': True,
    'auto_install': False,
}