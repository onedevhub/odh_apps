# -*- coding: utf-8 -*-
# Part of OneDevHub.

{
    'name': "Sale Line BOM Overview",
    'version': '18.0.1.0.1',
    'category': 'Manufacturing',
    'author': 'OneDevHub',
    'website': 'https://onedevhub.in',
    'license': 'LGPL-3',
    'depends': ['sale_management',
                'mrp'],
    'data': [
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
