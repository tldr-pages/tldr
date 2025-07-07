# i2cset

> Set the value of a register of an I2C device.
> Note: All addresses should be specified in hexadecimal.
> More information: <https://manned.org/i2cdump>.

- Write to a register of an I2C device:

`i2cset {{i2cbus}} {{device_address}} {{register_address}} {{value}}`

- Write to a register of an I2C device without asking for confirmation:

`i2cset -y {{i2cbus}} {{device_address}} {{register_address}} {{value}}`

- Write to a register of an I2C device using a specific mode (`b`, `w`):

`i2cset {{i2cbus}} {{device_address}} {{register_address}} {{value}} {{mode}}`
