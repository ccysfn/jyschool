# -*- coding: utf-8 -*-
from odoo import http

# class Jyschool(http.Controller):
#     @http.route('/jyschool/jyschool/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/jyschool/jyschool/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('jyschool.listing', {
#             'root': '/jyschool/jyschool',
#             'objects': http.request.env['jyschool.jyschool'].search([]),
#         })

#     @http.route('/jyschool/jyschool/objects/<model("jyschool.jyschool"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('jyschool.object', {
#             'object': obj
#         })