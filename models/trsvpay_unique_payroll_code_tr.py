from odoo import models, fields


class TrsvpayUniquePayrollCodeTr(models.Model):
    _name = "trsvpay.unique.payroll.code.tr"
    _description = "Código de Planilla Única"

    code = fields.Char(string="Código", required=True)
    name = fields.Char(string="Nombre", required=True)
