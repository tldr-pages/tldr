# dmidecode

> Muestra los contenidos del DMI (conocido también como SMBIOS) en un formato legible por humanos.
> Require de privilegios de root.
> Más información: <https://manned.org/dmidecode>.

- Muestra todos los contenidos de la tabla DMI:

`sudo dmidecode`

- Muestra la versión de la BIOS:

`sudo dmidecode -s bios-version`

- Muestra el número de serie del equipo:

`sudo dmidecode -s system-serial-number`

- Muestra información de la BIOS:

`sudo dmidecode -t bios`

- Muestra información de la CPU:

`sudo dmidecode -t processor`

- Muestra información de la memoria:

`sudo dmidecode -t memory`
