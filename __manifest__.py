{
    'name': 'Acceso a Planilla Unica Custom',
    'version': '16.0.1.0.0',
    'description': 'Habilita el acceso a Planilla Única (Especiales) por defecto para todos los usuarios.',
    'summary': 'Módulo custom para saltar restricción de permisos en Planillas Especiales',
    'author': 'MRG',
    'depends': ['base', 'treming_sv_payroll'],
    'data': [
        'security/ir.model.access.csv',
        'data/res_groups.xml',
        'views/trsvpay_unique_payroll_code_tr.xml',
        'data/trsvpay_unique_payroll_code_tr.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
