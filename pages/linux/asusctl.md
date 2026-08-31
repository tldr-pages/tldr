# asusctl

> Control ASUS ROG and TUF laptop settings on Linux.
> More information: <https://asus-linux.org/asusctl/>.

- Display the current power and fan profile:

`asusctl profile -p`

- Switch to the next power and fan profile:

`asusctl profile -n`

- Set a specific power and fan profile:

`asusctl profile -s {{Quiet|Balanced|Performance}}`

- Set the keyboard LED backlight mode:

`asusctl led-mode {{static|breathe|rainbow|pulse}}`

- Set the battery charge threshold limit:

`asusctl -c {{80}}`

- Display the current GPU graphics mode:

`asusctl graphics -g`

- Set the screen panel overdrive state:

`asusctl bios --panel-od {{true|false}}`

- Display current system information and capabilities:

`asusctl info`
