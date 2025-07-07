# i2cdump

> Dump I2C device registers.
> Note: All addresses should be specified in hexadecimal.
> More information: <https://github.com/mozilla-b2g/i2c-tools/tree/master>.

- Dump all registers of an I2C device:

`i2cdump {{i2cbus}} {{device_address}}`

- Dump all registers of an I2C device without asking for confirmation:

`i2cdump -y {{i2cbus}} {{device_address}}`

- Dump all registers of an I2C device using a specific mode (`b`, `w`):
`i2cdump {{i2cbus}} {{device_address}} {{mode}}`

- Dump registers from `start` to `end` of an I2C device:
`i2cdump -r {{start}}-{{end}} {{i2cbus}} {{device_address}}`

