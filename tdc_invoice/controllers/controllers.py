# -*- coding: utf-8 -*-
from odoo import http

# class TdcInvoice(http.Controller):
#     @http.route('/tdc_invoice/tdc_invoice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tdc_invoice/tdc_invoice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tdc_invoice.listing', {
#             'root': '/tdc_invoice/tdc_invoice',
#             'objects': http.request.env['tdc_invoice.tdc_invoice'].search([]),
#         })

#     @http.route('/tdc_invoice/tdc_invoice/objects/<model("tdc_invoice.tdc_invoice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tdc_invoice.object', {
#             'object': obj
#         })