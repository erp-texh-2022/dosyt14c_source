# -*- coding: utf-8 -*-
# Part of dosyt. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ServiceTaxRate(models.Model):
    _name = "l10n_eu_service.service_tax_rate"
    _description = "EU Service Tax Rate"

    country_id = fields.Many2one('res.country', string='Country')
    rate = fields.Float(string="VAT Rate")
