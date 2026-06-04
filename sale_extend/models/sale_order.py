from odoo import fields, models


class SaleOrder(models.Model):
    """Extend sale.order with custom fields."""

    _inherit = "sale.order"

    xyz = fields.Char(
        help="Custom XYZ value for the sales order.",
    )
