# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo import exceptions

from datetime import date

class NCFBank(models.Model):
    _name = 'ncf_bank.report'

    name = fields.Char()
    account_journal_id = fields.Many2one(comodel_name="account.journal", string="Diario de compra", required=True, )
    partner_id = fields.Many2one(comodel_name="res.partner", string="Proveedor", required=True, )
    date = fields.Date(string="Fecha", required=False, default=date.today())
    line_bank_ids = fields.One2many(comodel_name="ncf_bank.report.line",
                                    inverse_name="bank_report_id",
                                    string="Lineas de gastos",
                                    required=False, )

    state = fields.Selection(string="Estado", selection=[('draft', 'Borrador'), ('done', 'Confirmado'), ('invoiced', 'Facturado') ],
                             required=False, default='draft')
    @api.model
    def create(self, values):
        # Add code here
        seq = self.env['ir.sequence'].next_by_code('ncf_bank.report')
        values['name'] = seq

        return super(NCFBank, self).create(values)

    @api.one
    def confirm_button(self):
        self.state = 'done'

    def create_invoice(self):

        for line in self.line_bank_ids:
            self.env['account.invoice'].create(
                {
                    'partner_id': self.partner_id.id,
                    'journal_id': self.account_journal_id.id,
                    'purchase_fiscal_type': '07',
                    'move_name': line.name,
                    'invoice_line_ids': [(0,0, {'name': line.description,
                                                'account_id': line.account_id.id,
                                                'price_unit':line.amount})],
                    'date_invoice': line.date,
                    'type': 'in_invoice'
                }

            )
        self.state = 'invoiced'

    def unlink(self):
        for i in self:
            if i.state != 'draft':
                raise exceptions.AccessError('No se puede eliminar un registro confirmado.')
            else:
                return super(NCFBank, self).unlink()

class NFCBankLine(models.Model):
    _name = 'ncf_bank.report.line'

    name = fields.Char(required=True)
    account_id = fields.Many2one(comodel_name="account.account", string="Cuenta gastos", required=True, )
    amount = fields.Float(string="Monto",  required=True, default=0.0)
    description = fields.Char(string="Concepto", required=True, )
    date = fields.Date(string="Fecha", required=True, )
    bank_report_id = fields.Many2one(comodel_name="ncf_bank.report", string="Reporte de gastos", required=False, )