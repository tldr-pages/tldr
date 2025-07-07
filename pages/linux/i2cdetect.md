# i2cdetect

> Scan I2C buses.
> More information: <https://manned.org/i2cdump>.

- List active I2C buses:

`i2cdetect -l`

- Scan devices on an I2C bus:

`i2cdetect {{i2c_bus}}`

- Scan devices on an I2C bus without asking for confirmation:

`i2cdetect -y {{i2c_bus}}`
