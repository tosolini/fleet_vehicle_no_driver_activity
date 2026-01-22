# -*- coding: utf-8 -*-
from odoo import models


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    def write(self, vals):
        """
        Skip the default TODO activity created when the driver changes.

        The `fleet_vehicle_history_date_end` module already closes the previous
        driver history, so the TODO is redundant. We let the standard behavior
        run, then delete the specific activity right after.
        """
        # Track original drivers to detect changes
        changing_drivers = {}
        if 'driver_id' in vals and vals['driver_id']:
            for vehicle in self:
                if vehicle.driver_id and vehicle.driver_id.id != vals['driver_id']:
                    changing_drivers[vehicle.id] = vehicle.driver_id.name
        
        # Call the standard behavior (which creates the activity)
        res = super(FleetVehicle, self).write(vals)
        
        # Remove the freshly created TODO activities if a driver changed
        if changing_drivers:
            for vehicle in self.filtered(lambda v: v.id in changing_drivers):
                driver_name = changing_drivers[vehicle.id]
                activities_to_remove = self.env['mail.activity'].search([
                    ('res_id', '=', vehicle.id),
                    ('res_model', '=', 'fleet.vehicle'),
                    ('activity_type_id', '=', self.env.ref('mail.mail_activity_data_todo').id),
                    ('note', 'ilike', driver_name),  # Note contains the previous driver name
                ])
                if activities_to_remove:
                    activities_to_remove.unlink()
        
        return res
