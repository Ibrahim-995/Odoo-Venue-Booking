

from odoo import api, fields, models, _


class OrderDetails(models.Model):
    _name = 'order.details'

    order_id = fields.Char('Order ID', required=True)
    name = fields.Char('Customer Name', required=True)
    email = fields.Char('Email')
    phone = fields.Char('Phone', required=True)
    address = fields.Char('Address', required=True)
    venue_name = fields.Char('Venue Name', required=True)
    venue_capacity = fields.Char('Venue Capacity', required=True)
    payment_method = fields.Selection([('credit_card', 'Credit Card'), (
        'cash', 'Cash'), ('bkash', 'B-Kash'), ('paypal', 'Paypal')], 'Payment Method')
    order_date = fields.Date(string='Order Date', date_format='%Y-%m-%d')
    shift = fields.Selection([('lunch', 'Lunch'), ('dinner', 'Dinner')],'Shedule')
