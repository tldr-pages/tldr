# nwipe

> Securely erase disks using a variety of recognized methods.
> More information: <https://manned.org/nwipe>.

- Launch the interactive Ncurses interface:

`sudo nwipe`

- Wipe specific devices using the default method (DoD 3-pass) without confirmation prompts:

`sudo nwipe --autonuke {{/dev/sdX /dev/sdY ...}}`

- Wipe a specific disk using a custom erasing method:

`sudo nwipe --method={{zero|one|gutmann|dod522022m}} {{/dev/sdX}}`

- Wipe a disk and power off the system upon completion:

`sudo nwipe --autonuke --autopoweroff {{/dev/sdX}}`

- Display version:

`nwipe --version`
