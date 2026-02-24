from odoo.addons.treming_sv_payroll.models.hr_employer_contributions import employer_target

# Parche de prevención de errores:
# Treming busca el Tipo Patronal seleccionado en su diccionario interno `employer_target`.
# Como agregamos 'unica', debemos enseñarle cómo manejar esa llave vacía para evitar un KeyError.
if 'unica' not in employer_target:
    employer_target['unica'] = []

from . import trsvpay_unique_payroll_code_tr
from . import hr_employer_contributions_custom
from . import hr_contract
