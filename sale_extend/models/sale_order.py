from odoo import fields, models


class SaleOrder(models.Model):
    """Extend sale.order with custom fields."""

    _inherit = "sale.order"

    xyz = fields.Char(
        string="XYZ",
        help="Custom character field on the sales order.",
    )
