# -*- coding: utf-8 -*-
from odoo import models, fields , api


class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    customer_owner_id = fields.Many2one('res.partner', string='Cliente propietario del Equipamento')