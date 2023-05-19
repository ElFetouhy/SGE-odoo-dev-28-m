# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Tareas(models.Model):
    _name = 'ie.tareas'
    _description = 'ie.tareas.descripcion'
    name = fields.Char(string='Nombre de la tarea',required=True)
    proyecto_id = fields.Many2one('ie.proyecto', string='Proyecto asignado')
    fecha_finalizacion = fields.Date(string='Fecha de finalizacion de tarea')
    estado = fields.Selection([('unassigned','Unassigned'),('to do', 'To do'),
                               ('in progress','In progress'),('done','Done')], default='unassigned',string='Estado')
    prioridad = fields.Selection([('1','1'),('2','2'),('3','3'),('4','4')],string="Prioridad")
    user_id = fields.Many2one('res.users', string='Responsable')
    miembro_equipo = fields.Image(string='Imagen',max_width=100, max_height=100)
    notas = fields.Text(string='Notas')
    etiqueta_ids = fields.Many2many('ie.etiquetas', string='Etiquetas')
    