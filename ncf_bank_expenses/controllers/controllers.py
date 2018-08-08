# -*- coding: utf-8 -*-
from odoo import http

# class NcfBankExpenses(http.Controller):
#     @http.route('/ncf_bank_expenses/ncf_bank_expenses/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ncf_bank_expenses/ncf_bank_expenses/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ncf_bank_expenses.listing', {
#             'root': '/ncf_bank_expenses/ncf_bank_expenses',
#             'objects': http.request.env['ncf_bank_expenses.ncf_bank_expenses'].search([]),
#         })

#     @http.route('/ncf_bank_expenses/ncf_bank_expenses/objects/<model("ncf_bank_expenses.ncf_bank_expenses"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ncf_bank_expenses.object', {
#             'object': obj
#         })