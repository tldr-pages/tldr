# i2cget

> Read from an register of an I2C device.
> See also: `i2cdetect`, `i2cdump`, `i2cset`.
> Note: All addresses should be specified in hexadecimal.
> More information: <https://manned.org/i2cget>.

- Read from a register of an I2C device:

`i2cget {{i2cbus}} {{device_address}} {{register_address}}`

- Read from a register of an I2C device without asking for confirmation:

`i2cget -y {{i2cbus}} {{device_address}} {{register_address}}`

- Read from a register of an I2C device using a specific mode:

`i2cget {{i2cbus}} {{device_address}} {{register_address}} {{b|w|c|s|i}}`
