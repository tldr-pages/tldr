# ddcutil

> Control the settings of connected displays via DDC/CI.
> This command requires the kernel module `i2c-dev` to be loaded.
> See also: `modprobe`.
> More information: <https://www.ddcutil.com/commands/>.

- List all compatible displays:

`ddcutil {{[det|detect]}}`

- Query the first compatible display for capabilities:

`ddcutil {{[cap|capabilities]}}`

- Change the brightness (option `10`) of display 1 to 50%:

`ddcutil {{[-d|--display]}} 1 {{[set|setvcp]}} 10 50`

- Increase the contrast (option `12`) of display 1 by 5%:

`ddcutil {{[-d|--display]}} 1 {{[set|setvcp]}} 12 + 5`

- Change the display source (option `60`) of a display:

`ddcutil {{[-d|--display]}} {{1}} {{[set|setvcp]}} 60 0x{{0f}}`

- Read the settings of display 1:

`ddcutil {{[-d|--display]}} 1 {{[get|getvcp]}} ALL`
