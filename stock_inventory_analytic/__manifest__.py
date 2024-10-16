# Copyright 2019 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    'name': "Stock Inventory Analytic",
    'summary': """
        Stock Inventory Analytic """,
    'author': 'Eficent, Odoo Community Association (OCA)',
    'website': "https://github.com/OCA/account-analytic",
    'category': 'Warehouse Management',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'depends': [
        'analytic',
        'stock_analytic',
        'stock_account',
    ],
    'data': [
        'views/stock_inventory_line_view.xml',
        'wizard/stock_product_change_qty.xml',
    ],
    'installable': True,
}
