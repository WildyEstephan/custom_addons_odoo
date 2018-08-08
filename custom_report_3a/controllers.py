# -*- coding: utf-8 -*-
from openerp import http

# class CustomReport3a(http.Controller):
#     @http.route('/custom_report_3a/custom_report_3a/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_report_3a/custom_report_3a/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_report_3a.listing', {
#             'root': '/custom_report_3a/custom_report_3a',
#             'objects': http.request.env['custom_report_3a.custom_report_3a'].search([]),
#         })

#     @http.route('/custom_report_3a/custom_report_3a/objects/<model("custom_report_3a.custom_report_3a"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_report_3a.object', {
#             'object': obj
#         })