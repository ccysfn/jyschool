# -*- coding: utf-8 -*-

from odoo import models, fields, api

class teacher(models.Model):
    _name = 'jyschool.teacher'
    _inherits = {'res.partner': 'partner_id'}

    name = fields.Char(related='partner_id.name',string='代号', inherited=True)
    sub = fields.Many2one('jyschool.subject',string='特长学科')