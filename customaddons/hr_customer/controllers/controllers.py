# -*- coding: utf-8 -*-
from odoo import http


class HrCustomer(http.Controller):
    @http.route('/hr_customer/hr_customer', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/hr_customer/hr_customer/objects', auth='public')
    def list(self, **kw):
        return http.request.render('hr_customer.listing', {
            'root': '/hr_customer/hr_customer',
            'objects': http.request.env['hr_customer.hr_customer'].search([]),
        })

    @http.route('/hr_customer/hr_customer/objects/<model("hr_customer.hr_customer"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('hr_customer.object', {
            'object': obj
        })
