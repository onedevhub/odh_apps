# -*- coding: utf-8 -*-
# Copyright (C) OneDevHub.

from odoo import models, fields, api


class Partner(models.Model):
    """
    Adds custom Customer and Vendor flags.
    Child contacts automatically inherit customer/vendor flags from their parent company.
    These flags remain synchronized with parent updates for data consistency.
    """

    _inherit = "res.partner"

    odh_customer = fields.Boolean(
        string="Customer",
        default=True,
        help="Enable this option if the contact is a customer. "
             "This allows you to create sales orders, invoices, "
             "and track receivables for this contact."
    )

    odh_vendor = fields.Boolean(
        string="Vendor",
        default=False,
        help="Enable this option if the contact is a vendor or supplier. "
             "This allows you to create purchase orders, vendor bills, "
             "and track payables for this contact."
    )

    @api.model_create_multi
    def create(self, vals_list):
        """
        When creating child contacts, inherit Customer/Vendor
        flags from the parent if not explicitly set.
        """
        for vals in vals_list:
            if vals.get('parent_id'):
                parent = self.browse(vals['parent_id'])

                # Inherit customer flag from parent
                if not vals.get('odh_customer') and parent.odh_customer:
                    vals['odh_customer'] = True

                # Inherit vendor flag from parent
                if not vals.get('odh_vendor') and parent.odh_vendor:
                    vals['odh_vendor'] = True
        return super().create(vals_list)

    def write(self, vals):
        """
        When updating Customer/Vendor flags on a partner,
        propagate the same values to its direct children.
        """
        result = super().write(vals)

        # If customer or vendor changed, update all child records
        if 'odh_customer' in vals or 'odh_vendor' in vals:
            for partner in self:
                # Update only direct children (not recursive)
                if partner.child_ids:
                    update_vals = {}
                    if 'odh_customer' in vals:
                        update_vals['odh_customer'] = vals['odh_customer']
                    if 'odh_vendor' in vals:
                        update_vals['odh_vendor'] = vals['odh_vendor']

                    # Update direct children
                    partner.child_ids.write(update_vals)

        return result