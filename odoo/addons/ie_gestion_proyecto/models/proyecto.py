# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Proyecto(models.Model):
    _name = 'ie.proyecto'
    _description = 'ie.proyecto.descripcion'
    name = fields.Char(string='Nombre del proyecto',required=True)
    _sql_constraints = [
        ("name_check", "unique (name)", "El nombre del proyecto ya existe!"),
    ]
    descripcion = fields.Text(string='Descripcion')
    imagen_proyecto = fields.Image('img', max_width=100, max_height=100)
    tarea_ids  = fields.One2many('ie.tareas', 'proyecto_id', string='Tareas')

    
    
    #Constrain para no repetir nombre de proyectos
    #@api.constrains('nombre_proyecto')
    #def _constrains_nombre_proyecto(self):
    #    pass
