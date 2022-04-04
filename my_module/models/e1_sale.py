# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SOL(models.Model):
    _inherit = 'sale.order.line'
    _name = _inherit

    e1_test = fields.Char(size=10)
    
    
class AccountMove(models.Model):
    _inherit = 'sale.order'
    _name = _inherit

    client_order_ref = fields.Char(size=60)