{
    'name': 'Elite Customizations',
    'version': '1.0.0',
    'author': 'santiago.paya@gestecad.com',
    #'description': """ """,
    'installable': True,
    'application': False,
    'license': 'AGPL-3',
    'category': 'Customizations',
    'depends': ['base', 'sale', 'account'],
    'data': [
        'data/base.report_paperformat_data_elite.xml',
        'data/account.email_template_edi_invoice_elite.xml',
        'views/sale.report_saleorder_document_elite.xml',
        'data/base.action_clean_es_address.xml'
    ],
}
