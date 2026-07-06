# sensors

> Report sensors information.
> See also: `btm`, `btop`.
> More information: <https://manned.org/sensors>.

- Show the current readings of all sensor chips:

`sensors`

- Show temperatures in degrees Fahrenheit:

`sensors {{[-f|--fahrenheit]}}`

- Show the readings of a specific sensor chip:

`sensors {{chip}}`

- Output sensor data in JSON format:

`sensors -j`

- Show raw sensor output for scripting or debugging purposes:

`sensors -u`

- Show sensor readings using a specific configuration file:

`sensors --config-file {{path/to/sensors.conf}}`

- List all detected hardware communication buses (like I2C or ISA):

`sensors --bus-list`
