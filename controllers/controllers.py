# -*- coding: utf-8 -*-
from odoo import http

# class MxCMedicale(http.Controller):
#     @http.route('/mxcmedicale/mxcmedicale/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mxcmedicale/mxcmedicale/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mxcmedicale.listing', {
#             'root': '/mxcmedicale/mxcmedicale',
#             'objects': http.request.env['mxcmedicale.mxcmedicale'].search([]),
#         })

#     @http.route('/mxcmedicale/mxcmedicale/objects/<model("mxcmedicale.mxcmedicale"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mxcmedicale.object', {
#             'object': obj
#         })