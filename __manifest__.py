# -*- coding: utf-8 -*-
{
    'name': "vn_purchase_forecast_report",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['purchase','purchase_requisition'],

    # always loaded
    'data': [
        'security/banque_security.xml',
        'security/ir.model.access.csv',
        #'report/purchase_forecast_report.xml',
        #'report/purchase_forecast_templete.xml',
        #'purchase_requisition_repport.xml',
        #'views/raport_purchase_requisition.xml',
        'report/purchase_requisition_report_views.xml',
       
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
