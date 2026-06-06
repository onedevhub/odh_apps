# -*- coding: utf-8 -*-
# Part of OneDevHub.

{
    'name': "Sale Line BOM Overview",
    'version': '17.0.1.0.0',
    'category': 'Manufacturing',
    'summary': """ Quickly view the Bill of Materials (BOM) overview directly from Sales Orders without navigating through products or manufacturing menus """,
    'description': """ Quickly view the Bill of Materials (BOM) overview directly from Sales Orders without navigating through products or manufacturing menus """,
    'author': 'OneDevHub',
    'website': 'https://onedevhub.in',
    'license': 'OPL-1',
    'depends': ['sale_management', 'mrp'],
    'data': [
        'views/sale_order_views.xml',

    ],
    "price": "5.00",
    "currency": "USD",
    "images": ["static/description/app_img/banner_image.jpg"],
    'installable': True,
    'application': True,
    'auto_install': False,

}
