# -*- encoding: utf-8 -*-
# Part of dosyt. See LICENSE file for full copyright and licensing details.
{
    'name': 'K.S.A - Invoice',
    'version': '1.0.0',
    'author': 'dosyt ERP',
    'category': 'Accounting/Localizations',
    'license': 'LGPL-3',
    'description': """
    Invoices for the Kingdom of Saudi Arabia
""",
    'depends': ['l10n_sa', 'l10n_gcc_invoice'],
    'data': [
        'views/view_move_form.xml',
        'views/report_invoice.xml',
    ],
}
