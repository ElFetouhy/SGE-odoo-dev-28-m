from odoo import models, fields, api

class Estado(models.Model):
    _name = 'ie.estado'
    _description = 'ie.estado.description'
    #field_name_ids = fields.One2many('comodel_name', 'inverse_field_name', string='field_name')