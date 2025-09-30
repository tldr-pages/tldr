# i2cdetect

> Scan I2C buses.
> See also: `i2cdump`, `i2cget`, `i2cset`.
> More information: <https://manned.org/i2cdetect>.

- List active I2C buses:

`i2cdetect -l`

- Scan devices on an I2C bus:

`i2cdetect {{i2c_bus}}`

- Scan devices on an I2C bus without asking for confirmation:

`i2cdetect -y {{i2c_bus}}`
