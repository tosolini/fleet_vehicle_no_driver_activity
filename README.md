# Fleet Vehicle - No Driver Activity

## Overview

This module removes the automatic "Specify the end date" TODO activity that is created when a vehicle driver changes.

## Why

The companion module `fleet_vehicle_history_date_end` already closes the previous driver history automatically. The default TODO becomes redundant and adds noise.

## Features

- Prevents the TODO activity when a new driver is assigned to a vehicle
- Leaves all other fleet behaviors unchanged
- Compatible with `fleet_vehicle_history_date_end`

## Installation

1. Depends on `fleet` and `fleet_vehicle_history_date_end`
2. Install from Apps or update the module list and install

## License

LGPL-3.0 or later

### Maintainer
This module is maintained by the community. For issues or contributions, please use the GitHub repository.

## Author

Walter Tosolini
