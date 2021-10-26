# dmidecode

> Muestra la tabla de contenidos del DMI (también conocido como SMBIOS) en un formato legible por humanos.
> Require de privilegios de root.
> Más información: <https://manned.org/dmidecode>.

- Muestra todos la tabla de contenidos de DMI:

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
