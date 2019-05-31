# -*- coding: utf-8 -*-

from odoo import models, fields, api

class subject(models.Model):
    _name = 'jyschool.subject'

    name = fields.Char()
    