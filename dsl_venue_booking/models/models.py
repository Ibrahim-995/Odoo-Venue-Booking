from odoo import models, fields, api

class Venue(models.Model):
    _name = 'dsl.venue'
    
    name = fields.Char(string='Name', required=True)
    capacity = fields.Integer(string='Capacity', required=True)
    description = fields.Text(string='Description')
    image = fields.Binary(string='Image')

