# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 Open Business Solutions (<http://www.obsdr.com>)
#    Author: Naresh Soni
#    Copyright 2015 Cozy Business Solutions Pvt.Ltd(<http://www.cozybizs.com>)
#    Copyright (C) 2010-Today OpenERP SA (<http://www.openerp.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

from openerp import models, fields, api

class TheAmount(models.Model):
    _inherit = 'account.voucher'

    def removeDecimal(self,monto):
        strMonto = str(monto)
        return strMonto.split('.')

    @api.model
    def withComa(self, monto):
        unDecimal, decimal = self.removeDecimal(monto)

        tam = len(unDecimal)
        undo = 0
        listo = []
        for l in unDecimal:
            listo.append(l)

        while True:
            if tam > 3:
                tam -= 3
                listo.insert(tam, ',')
            else:
                break

        return ''.join(listo) + '.' + decimal


