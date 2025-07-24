# hddtemp

> Display temperature of HDD via S.M.A.R.T.
> More information: <https://manned.org/hddtemp>.

- Display temperature of a specific drive:

`hddtemp {{type}}:{{/dev/sdX}}`

- Display temperature of a SATA drive assigned to `sda`:

`hddtemp SATA:/dev/sda`

- Log temperatures to syslog every `n` seconds:

`hddtemp {{[-S|--syslog]}} {{nseconds}} {{type}}:{{/dev/sdX}}`

- Print only numeric value of temperature without unit:

`hddtemp {{[-n|--numeric]}} {{type}}:{{/dev/sdX}}`

- Define the unit used to denote temperature:

`hddtemp {{[-u|--unit]}} {{C|F}} {{type}}:{{/dev/sdX}}`

- Wake ATA drive before attempting to read temperature:

`hddtemp {{[-w|--wake-up]}} {{type}}:{{/dev/sdX}}`

- Enter debug mode to show S.M.A.R.T. fields and their values:

`hddtemp {{[-D|--debug]}} {{type}}:{{/dev/sdX}}`

- Suppress compatibility check for drive types:

`hddtemp {{[-q|--quiet]}} {{type}}:{{/dev/sdX}}`
