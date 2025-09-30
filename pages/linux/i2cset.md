# i2cset

> Set the value of a register of an I2C device.
> See also: `i2cdetect`, `i2cdump`, `i2cget`.
> Note: All addresses should be specified in hexadecimal.
> More information: <https://manned.org/i2cset>.

- Write to a register of an I2C device:

`i2cset {{i2cbus}} {{device_address}} {{register_address}} {{value}}`

- Write to a register of an I2C device without asking for confirmation:

`i2cset -y {{i2cbus}} {{device_address}} {{register_address}} {{value}}`

- Write to a register of an I2C device using a specific mode:

`i2cset {{i2cbus}} {{device_address}} {{register_address}} {{value}} {{b|w|c|s|i}}`
