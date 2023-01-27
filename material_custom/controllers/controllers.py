# -*- coding: utf-8 -*-
# from odoo import http


# class .\project\belajar\materialCustom(http.Controller):
#     @http.route('/.\project\belajar\material_custom/.\project\belajar\material_custom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/.\project\belajar\material_custom/.\project\belajar\material_custom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('.\project\belajar\material_custom.listing', {
#             'root': '/.\project\belajar\material_custom/.\project\belajar\material_custom',
#             'objects': http.request.env['.\project\belajar\material_custom..\project\belajar\material_custom'].search([]),
#         })

#     @http.route('/.\project\belajar\material_custom/.\project\belajar\material_custom/objects/<model(".\project\belajar\material_custom..\project\belajar\material_custom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('.\project\belajar\material_custom.object', {
#             'object': obj
#         })
