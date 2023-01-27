# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Material(models.Model):
    _name = 'res.material'
    _description = 'Model yang didalamnya berfungsi untuk melakukan registrasi material yang akan dijual'

    name = fields.Char(required=True)
    code = fields.Char(required=True)
    partner_id = fields.Many2one(comodel_name="res.partner",
                                 required=True)
    type = fields.Selection(selection=[('fabric', 'Fabric'),
                                       ('jeans', 'Jeans'),
                                       ('cotton', 'Cotton'),],
                            required=True)
    company_id = fields.Many2one(comodel_name="res.company",
                                 default=lambda self: self.env.company)
    currency_id = fields.Many2one(comodel_name="res.currency",
                                  related="company_id.currency_id")
    buy_price = fields.Monetary(currency_field="currency_id",
                                required=True)

    @api.constrains("buy_price")
    def _check_buy_price(self):
        for record in self:
            if record.buy_price < 100:
                raise ValidationError(
                    _("Material buy price tidak boleh nilainya < 100"))
