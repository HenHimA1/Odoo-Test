from odoo.tests import TransactionCase
from odoo.exceptions import UserError, ValidationError


class TestResMaterial(TransactionCase):
    def setUp(self):
        super(TestResMaterial, self).setUp()
        self.res_material_obj = self.env["res.material"]
        vals = {
            "name": "Test Material",
            "code": "Test Material Code",
            "partner_id": self.env.ref("base.res_partner_4").id,
            "type": "jeans",
            "buy_price": 250,
        }
        self.res_material = self.res_material_obj.create(vals)
    
    def test_buy_price_res_material(self):
        res_material = self.res_material
        
        # Material buy price tidak boleh nilainya < 100
        with self.assertRaises(ValidationError):
            res_material.write({"buy_price": 50})
