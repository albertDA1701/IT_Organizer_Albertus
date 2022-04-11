# -*- coding: utf-8 -*-
{
    'name': "it_organizer",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',
    'application':True, 

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/hp_views.xml',
        'views/laptop_views.xml',
        'views/tv_views.xml',
        'views/tv_views.xml',
        'views/peralatandapur_views.xml',
        'views/peralatan_rmhtangga_views.xml',
        'views/orderbaranghp_views.xml',
        'views/pegawai_views.xml',
        'views/orderbaranglaptop_views.xml',
        'views/orderbarangtv_views.xml',
        'views/orderbarangdapur_views.xml',
        'views/orderbarang_rmhtangga_views.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
