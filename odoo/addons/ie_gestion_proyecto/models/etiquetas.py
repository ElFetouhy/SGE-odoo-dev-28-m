# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Etiquetas(models.Model):
    _name = 'ie.etiquetas'
    _description = 'ie.etiquetas.description'
    name = fields.Char(string='Nombre de etiqueta',required=True)
    # tarea_id = fields.Many2one('ie.tareas', string='Tarea')
    tarea_ids = fields.Many2many('ie.tareas', string='Tarea')