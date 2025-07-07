# i2cget

> Read from an register of an I2C device.
> Note: All addresses should be specified in hexadecimal.
> More information: <https://manned.org/i2cdump>.

- Read from a register of an I2C device:

`i2cget {{i2cbus}} {{device_address}} {{register_address}}`

- Read from a register of an I2C device without asking for confirmation:

`i2cget -y {{i2cbus}} {{device_address}} {{register_address}}`

- Read from a register of an I2C device using a specific mode (`b`, `w`):

`i2cget {{i2cbus}} {{device_address}} {{register_address}} {{mode}}`
