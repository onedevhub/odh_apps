# -*- coding: utf-8 -*-
# Copyright (C) OneDevHub.

from odoo import api, fields, models

class SaleOrder(models.Model):
    """
    Enables customer flag for partners when used in sales orders.
    """

    _inherit = "sale.order"


    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            partner_id = vals.get('partner_id')
            if partner_id:
                partner = self.env['res.partner'].browse(partner_id)
                if not partner.odh_customer:
                    partner.write({'odh_customer': True})
        return super().create(vals_list)

    def write(self, vals):
        """Check and update customer flags when partner is changed"""
        if vals.get('partner_id'):
            for record in self:
                partner = self.env['res.partner'].browse(vals['partner_id'])
                if not partner.odh_customer:
                    partner.write({'odh_customer': True})
        return super().write(vals)
