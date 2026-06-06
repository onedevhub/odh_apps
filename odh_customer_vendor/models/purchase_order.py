# -*- coding: utf-8 -*-
# Copyright (C) OneDevHub.

from odoo import api, fields, models

class PurchaseOrder(models.Model):
    """
    Enables vendor flag on partners when they're used in purchase orders.
    """

    _inherit = "purchase.order"

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            partner_id = vals.get('partner_id')
            if partner_id:
                partner = self.env['res.partner'].browse(partner_id)
                if not partner.odh_vendor:
                    partner.write({'odh_vendor': True})
        return super().create(vals_list)

    def write(self, vals):
        """Check and update new partner as vendor when changing PO partner."""
        if vals.get('partner_id'):
            for record in self:
                partner = self.env['res.partner'].browse(vals['partner_id'])
                if not partner.odh_vendor:
                    partner.write({'odh_vendor': True})
        return super().write(vals)

