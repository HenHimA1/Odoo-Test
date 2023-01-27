# -*- coding: utf-8 -*-
{
    'name': "Material Custom",

    'summary': """
        Modul Odoo yang didalamnya berfungsi untuk melakukan registrasi material yang akan dijual""",

    'description': """
        Modul Odoo yang didalamnya berfungsi untuk melakukan registrasi material yang akan dijual
    """,

    'author': "Hendra Himawan",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '15.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/res_material_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
