# -*- coding: utf-8 -*-

from odoo import models, fields, api
import number_to_word

# class tdc_invoice(models.Model):
#     _name = 'tdc_invoice.tdc_invoice'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class TDCInvoice(models.Model):
    _inherit = 'account.invoice'

    amount_in_word = fields.Char(string="Monto En letras", required=False, compute="_compute_amount_in_word", store=True)

    @api.one
    @api.depends('amount_total')
    def _compute_amount_in_word(self):
        """
        @api.depends() should contain all fields that will be used in the calculations.
        """
        self.amount_in_word = number_to_word.to_word(self.amount_total, self.currency_id.name)