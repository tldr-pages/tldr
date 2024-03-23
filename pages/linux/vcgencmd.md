# vcgencmd

> Print system information for a Raspberry Pi.
> More information: <https://www.raspberrypi.org/documentation/computers/os.html#vcgencmd>.

- List all available commands:

`vcgencmd commands`

- Print the current CPU temperature:

`vcgencmd measure_temp`

- Print the current voltage:

`vcgencmd measure_volts`

- Print the throttled state of the system as a bit pattern:

`vcgencmd get_throttled`

- Print the bootloader configuration (only available on Raspberry Pi 4 models):

`vcgencmd bootloader_config`

- Display help:

`vcgencmd --help`
