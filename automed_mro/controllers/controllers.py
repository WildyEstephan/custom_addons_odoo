# -*- coding: utf-8 -*-
from odoo import http

# class AutomedMro(http.Controller):
#     @http.route('/automed_mro/automed_mro/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/automed_mro/automed_mro/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('automed_mro.listing', {
#             'root': '/automed_mro/automed_mro',
#             'objects': http.request.env['automed_mro.automed_mro'].search([]),
#         })

#     @http.route('/automed_mro/automed_mro/objects/<model("automed_mro.automed_mro"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('automed_mro.object', {
#             'object': obj
#         })