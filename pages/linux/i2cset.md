# i2cset

> I2C bus register writing tool.
> Note: All addresses should be specified in hexadecimal.
> More information: <https://github.com/mozilla-b2g/i2c-tools/tree/master>.

- Write to a register of an I2C device:

`i2cset {{i2cbus}} {{device_address}} {{register_address}} {{value}}`

- Write to a register of an I2C device without asking for confirmation:
`i2cset -y {{i2cbus}} {{device_address}} {{register_address}} {{value}}`

- Write to a register of an I2C device using a specific mode (`b`, `w`):

`i2cset {{i2cbus}} {{device_address}} {{register_address}} {{value}} {{mode}}`

