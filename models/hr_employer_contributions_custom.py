from odoo import models, fields

class HrPlanillaCustom(models.Model):
    _inherit = 'hr.planilla'

    employer_type = fields.Selection(
        selection_add=[('unica', 'Planilla Única')],
        ondelete={'unica': 'set null'}
    )

class HrPayslipEmployeesCustom(models.TransientModel):
    _inherit = 'hr.payslip.employees'

    employer_type = fields.Selection(
        selection_add=[('unica', 'Planilla Única')],
        ondelete={'unica': 'set null'}
    )
