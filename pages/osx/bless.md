# bless

> Set volume bootability and startup disk options.

- FOLDER MODE: bless a volume with only Mac OS X or Darwin, and create the BootX and boot.efi files as needed:

`bless --folder {{/Volumes/Mac OS X/System/Library/CoreServices}} --bootinfo --bootefi`

- MOUNT MODE: set a volume containing either Mac OS 9 and Mac OS X to be the active volume:

`bless --mount {{/Volumes/Mac OS}} --setBoot`

- NETBOOT MODE: set the system to NetBoot and broadcast for an available server:

`bless --netboot --server {{bsdp://255.255.255.255}}`

- INFO MODE: gather information about the currently selected volume (as determined by the firmware), suitable for piping to a program capable of parsing Property Lists:

`bless --info --plist`
