# -*- coding: utf-8 -*-
{
    'name': "NCF Bank Expenses",

    'summary': """
        Permite crear varias facturas para varios gastos bancarios""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Wildy Estephan",
    'website': "http://www.wildyestephan.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'ncf_manager', 'account', 'account_accountant'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'sequences/sequence.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}