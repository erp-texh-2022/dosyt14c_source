# -*- coding: utf-8 -*-
# Part of dosyt. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    sale_team_id = fields.Many2one(
        'crm.team', "User's Sales Team",
        help='Sales Team the user is member of. Used to compute the members of a Sales Team through the inverse one2many')