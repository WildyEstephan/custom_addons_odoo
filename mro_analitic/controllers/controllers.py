# -*- coding: utf-8 -*-
from odoo import http

# class MroAnalitic(http.Controller):
#     @http.route('/mro_analitic/mro_analitic/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mro_analitic/mro_analitic/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mro_analitic.listing', {
#             'root': '/mro_analitic/mro_analitic',
#             'objects': http.request.env['mro_analitic.mro_analitic'].search([]),
#         })

#     @http.route('/mro_analitic/mro_analitic/objects/<model("mro_analitic.mro_analitic"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mro_analitic.object', {
#             'object': obj
#         })