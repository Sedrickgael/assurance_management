# -*- coding: utf-8 -*-
# from odoo import http


# class AssuranceManagement(http.Controller):
#     @http.route('/assurance_management/assurance_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/assurance_management/assurance_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('assurance_management.listing', {
#             'root': '/assurance_management/assurance_management',
#             'objects': http.request.env['assurance_management.assurance_management'].search([]),
#         })

#     @http.route('/assurance_management/assurance_management/objects/<model("assurance_management.assurance_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('assurance_management.object', {
#             'object': obj
#         })
