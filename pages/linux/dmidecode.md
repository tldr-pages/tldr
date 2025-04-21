# dmidecode

> Display the DMI (alternatively known as SMBIOS) table contents in a human-readable format.
> Requires root privileges.
> More information: <https://manned.org/dmidecode>.

- Show all DMI table contents:

`sudo dmidecode`

- Show the BIOS version:

`sudo dmidecode {{[-s|--string]}} bios-version`

- Show the system's serial number:

`sudo dmidecode {{[-s|--string]}} system-serial-number`

- Show BIOS information:

`sudo dmidecode {{[-t|--type]}} bios`

- Show CPU information:

`sudo dmidecode {{[-t|--type]}} processor`

- Show memory information:

`sudo dmidecode {{[-t|--type]}} memory`
