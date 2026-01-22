# -*- coding: utf-8 -*-
from odoo.tests.common import SavepointCase


class TestNoDriverActivity(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.partner_driver_old = cls.env["res.partner"].create({"name": "Old Driver"})
        cls.partner_driver_new = cls.env["res.partner"].create({"name": "New Driver"})
        cls.brand = cls.env["fleet.vehicle.model.brand"].create({"name": "Brand"})
        cls.model = cls.env["fleet.vehicle.model"].create(
            {"name": "Model", "brand_id": cls.brand.id}
        )
        cls.vehicle = cls.env["fleet.vehicle"].create(
            {
                "model_id": cls.model.id,
                "driver_id": cls.partner_driver_old.id,
                "license_plate": "TEST123",
            }
        )

    def test_driver_change_does_not_create_todo_activity(self):
        """Changing driver should not leave the default TODO activity."""
        self.vehicle.write({"driver_id": self.partner_driver_new.id})
        activities = self.env["mail.activity"].search(
            [
                ("res_id", "=", self.vehicle.id),
                ("res_model", "=", "fleet.vehicle"),
                (
                    "activity_type_id",
                    "=",
                    self.env.ref("mail.mail_activity_data_todo").id,
                ),
            ]
        )
        self.assertFalse(
            activities,
            "The default TODO activity should be removed when the driver changes.",
        )
