# coding=utf-8

from openerp import models, fields, api


class res_partner(models.Model):

    _inherit = 'res.partner'


    # street 详细地址
    is_teacher = fields.Boolean('是否老师')
