from odoo import http
from odoo.http import request


class WebsiteVenue(http.Controller):

    @http.route('/venues', type='http', auth="public", website=True)
    def venue_list(self, **kw):
        venues = request.env['dsl.venue'].search([])
        return request.render('dsl_venue_booking.template_venue_web', {'venues': venues})

    @http.route(['/customer/details/<int:venue_id>'], type='http', auth="public", website=True)
    def customer_details(self, venue_id=None, **kw):
        venue = request.env['dsl.venue'].sudo().browse(venue_id)
        venue_name = venue.name
        venue_capacity = venue.capacity
        return request.render('dsl_venue_booking.template_customer_details', {
            'venue_name': venue_name,
            'venue_capacity': venue_capacity,
        })

    @http.route('/submit/details', type='http', auth="public", website=True)
    def submit_details(self, **kw):
        request.env['order.details'].sudo().create(kw)
        return request.render('dsl_venue_booking.thank_you_id', {})
