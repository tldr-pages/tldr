# dmidecode

> Display the DMI (alternatively known as SMBIOS) table contents in a human-readable format.
> Requires root privileges.

- Show all DMI table contents:

`sudo dmidecode`

- Show the BIOS version:

`sudo dmidecode -s bios-version`

- Show the system's serial number:

`sudo dmidecode -s system-serial-number`

- Show BIOS information:

`sudo dmidecode -t bios`

- Show CPU information:

`sudo dmidecode -t processor`

- Show memory information:

`sudo dmidecode -t memory`
