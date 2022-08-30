# -*- coding: utf-8 -*-
{
    'name': "Academy",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/student_view.xml',
        'views/teacher_view.xml',
        'views/subject_view.xml',
        'wizard/batch_update.xml',
        # 'reports/student_report_view.xml',
        'security/student_security.xml',
        'data/data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
        # 'demo/student_demo.xml',
    ],

    'installable': True,
    'application': True,
    'license': 'GPL-3',
}
