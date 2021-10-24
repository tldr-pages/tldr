# solo

> Interact with Solo hardware security keys.
> More information: <https://github.com/solokeys/solo-python>.

- List connected Solos:

`solo ls`

- Update the currently connected Solo's firmware to the latest version:

`solo key update`

- Blink the LED of a specific Solo:

`solo key wink --serial {{serial_number}}`

- Generate random bytes using the currently connected Solo's secure random number generator:

`solo key rng raw`

- Monitor the serial output of a Solo:

`solo monitor {{path/to/serial_port}}`
