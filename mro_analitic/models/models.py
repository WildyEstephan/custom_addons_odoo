# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date

# class mro_analitic(models.Model):
#     _name = 'mro_analitic.mro_analitic'
#
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100


class AssetAccount(models.Model):
    _inherit = 'asset.asset'

    account_analytic_id = fields.Many2one(comodel_name="account.analytic.account", string="Account Analytic", required=False, )

    @api.model
    def create(self, values):
        # Add code here
        account_id = self.env['account.analytic.account'].create(

            {
                'name': values['name'],
                'code': 'MRO'
            }
        )

        values['account_analytic_id'] = account_id.id

        return super(AssetAccount, self).create(values)

class AssetRequeestAccount(models.Model):
    _inherit = 'mro.request'

    account_analytic_id = fields.Many2one(comodel_name="account.analytic.account", string="Account Analytic", required=True,)

    @api.onchange('asset_id')
    def _onchange_asset_id(self):
        if self.asset_id.account_analytic_id:
            self.account_analytic_id = self.asset_id.account_analytic_id

class OrderAssetAccount(models.Model):
    _inherit = 'mro.order'
    account_analytic_id = fields.Many2one(comodel_name="account.analytic.account", string="Account Analytic", required=True, related='asset_id.account_analytic_id' )

    def action_done(self):

        res = super(OrderAssetAccount, self).action_done()

        order_lines = self.parts_lines

        for line in order_lines:

            qty = line.parts_qty
            cost = line.parts_id.standard_price
            amount = (qty * cost) * -1

            self.env['account.analytic.line'].create(
                {'name': self.asset_id.name,
                 'account_id': self.account_analytic_id.id,
                 'date': date.today(),
                 'amount': amount,
                 'product_id': line.parts_id.id,
                 'product_uom_id': line.parts_id.uom_id.id,
                 'ref': self.name,
                 'unit_amount': line.parts_qty
                 }
            )

        return res