# -*- coding: utf-8 -*-
# Part of dosyt. See LICENSE file for full copyright and licensing details.

from . import models
from odoo import api, SUPERUSER_ID


def _update_street_format(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['res.partner'].search([])._compute_street_data()
