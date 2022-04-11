# -*- coding: utf-8 -*-
# from odoo import http


# class ItOrganizer(http.Controller):
#     @http.route('/it_organizer/it_organizer/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/it_organizer/it_organizer/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('it_organizer.listing', {
#             'root': '/it_organizer/it_organizer',
#             'objects': http.request.env['it_organizer.it_organizer'].search([]),
#         })

#     @http.route('/it_organizer/it_organizer/objects/<model("it_organizer.it_organizer"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('it_organizer.object', {
#             'object': obj
#         })
