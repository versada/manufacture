# Copyright 2021 Versada UAB
# License AGPL-3 or later (https://www.gnu.org/licenses/agpl).

from odoo.tests.common import TransactionCase


class TestProductTemplate(TransactionCase):
    def test_compute_refurbish_product_wo_variant(self):
        product_tpl = (
            self.env["product.template"]
            .with_context(
                create_product_product=False,
            )
            .create(
                {
                    "name": "Test Product",
                }
            )
        )

        self.assertFalse(product_tpl.refurbish_product_id)
