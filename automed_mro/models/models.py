# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AutoMeter(models.Model):
    _inherit = 'mro.pm.meter'

    @api.model
    def create(self, values):
        # Add code here
        s = self.search([('name', '=', values['name']), ('asset_id','=', values['asset_id'])])


        if s:
            s = s[-1]
            if values['reading_type'] == 'inc':
                values['total_value'] = values['value'] + s['total_value']
            elif values['reading_type'] == 'dec':
                values['total_value'] = s['total_value'] - values['value']
            elif values['reading_type'] == 'cng':
                values['total_value'] = values['value']
        else:
            values['total_value'] = values['value']

        return super(AutoMeter, self).create(values)

class ReadingMeter(models.Model):
    _inherit = 'mro.order'

    parameter_id = fields.Many2one(comodel_name="mro.pm.parameter", string="Parametro", required=False, )
    meter = fields.Float(string="Medida",  required=False, )
    reading_type = fields.Selection(string="Tipo de lectura",
                             selection=[('inc', 'Incrementar'), ('dec', 'Decrementar'), ('cng', 'Cambiar'), ],
                             required=False, )
    @api.one
    def button_meter(self):
        self.env['mro.pm.meter'].create(
            {
                'name': self.parameter_id.id,
                'reading_type': self.reading_type,
                'value': self.meter,
                'av_time': 0.0,
                'asset_id': self.asset_id.id
            }
        )