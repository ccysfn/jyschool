# -*- coding: utf-8 -*-

from odoo import models, fields, api

class teacher(models.Model):
    _name = 'jyschool.teacher'
    _inherits = {'res.partner': 'partner_id'}

    sub = fields.Many2one('jyschool.subject',string='特长学科')