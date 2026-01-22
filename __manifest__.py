# -*- coding: utf-8 -*-
{
    'name': 'Fleet Vehicle - No Driver Activity',
    'version': '18.0.1.0.0',
    'category': 'Human Resources/Fleet',
    'summary': 'Disable the automatic TODO when the driver changes',
    'description': """
        Prevent the automatic creation of the "Specify the end date" TODO
        when a new driver is assigned to a vehicle.

        The companion module fleet_vehicle_history_date_end already closes
        the previous driver history automatically, so the manual activity
        is redundant.
    """,
    'author': 'Walter Tosolini',
    'website': 'https://www.tosolini.info',
    'depends': [
        'fleet',
        'fleet_vehicle_history_date_end',
    ],
    'data': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
