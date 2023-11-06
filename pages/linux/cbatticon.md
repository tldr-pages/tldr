# cbatticon

> A lightweight and fast battery icon that sits in your system tray.
> More information: <https://github.com/valr/cbatticon>.

- Show the battery icon in the system tray:

`cbatticon`

- Show the battery icon and set the update interval to 20 seconds:

`cbatticon --update-interval {{20}}`

- List available icon types:

`cbatticon --list-icon-types`

- Show the battery icon with a specific icon type:

`cbatticon --icon-type {{standard|notification|symbolic}}`

- List available power supplies:

`cbatticon --list-power-supplies`

- Show the battery icon for a specific battery:

`cbatticon {{BAT0}}`

- Show the battery icon and which command to execute when the battery level reaches the set critical level:

`cbatticon --critical-level {{5}} --command-critical-level {{poweroff}}`
