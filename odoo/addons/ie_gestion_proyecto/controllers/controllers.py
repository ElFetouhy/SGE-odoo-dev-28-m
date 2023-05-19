# -*- coding: utf-8 -*-
# from odoo import http


# class IeGestionProyecto(http.Controller):
#     @http.route('/ie_gestion_proyecto/ie_gestion_proyecto', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ie_gestion_proyecto/ie_gestion_proyecto/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ie_gestion_proyecto.listing', {
#             'root': '/ie_gestion_proyecto/ie_gestion_proyecto',
#             'objects': http.request.env['ie_gestion_proyecto.ie_gestion_proyecto'].search([]),
#         })

#     @http.route('/ie_gestion_proyecto/ie_gestion_proyecto/objects/<model("ie_gestion_proyecto.ie_gestion_proyecto"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ie_gestion_proyecto.object', {
#             'object': obj
#         })
