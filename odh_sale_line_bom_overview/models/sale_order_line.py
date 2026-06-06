# -*- coding: utf-8 -*-
# Copyright (C) OneDevHub.


from odoo import fields, models, api


class SaleOrderLine(models.Model):
    """Inherited model 'sale.order.line' and added required fields"""
    _inherit = 'sale.order.line'

    bom_id = fields.Many2one('mrp.bom', string='Bill of Materials',
                             help="Bill of materials for the product")

    product_template_id = fields.Many2one(related="product_id.product_tmpl_id",
                                          string="Template Id of Selected Product",
                                          help="Template id of the selected product")

    @api.onchange('product_id')
    def _onchange_product_id_clear_bom(self):
        """Clear BOM when product changes and set default if only one exists"""
        if self.product_id:
            # Get all BOMs for this product's template
            bom_domain = [
                ('product_tmpl_id', '=', self.product_id.product_tmpl_id.id),
                ('type', '=', 'normal')  # Only normal BOMs, not phantom/kit
            ]
            available_boms = self.env['mrp.bom'].search(bom_domain)

            # If there's only one BOM, set it automatically
            if len(available_boms) == 1:
                self.bom_id = available_boms.id
            # If current BOM doesn't match product template, clear it
            elif self.bom_id and self.bom_id.product_tmpl_id != self.product_id.product_tmpl_id:
                self.bom_id = False
            # If no BOMs exist, clear it
            elif not available_boms:
                self.bom_id = False

    def action_bom_overview(self):
        self.ensure_one()

        return {
            'type': 'ir.actions.client',
            'tag': 'mrp_bom_report',
            'name': 'BoM Overview',
            'context': {
                'active_id': self.bom_id.id,
                'active_ids': [self.bom_id.id],
                'active_model': 'mrp.bom',
            }
        }



