# -*- coding: utf-8 -*-

from odoo import models, fields, api

class classes(models.Model):
    _name = 'jyschool.classes'

    name = fields.Char()
    teacher = fields.Many2one('jyschool.teacher','授课老师')
    