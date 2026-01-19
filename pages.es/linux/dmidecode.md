# dmidecode

> Muestra la tabla de contenidos del DMI (también conocido como SMBIOS) en un formato legible por humanos.
> Requiere privilegios de root.
> Más información: <https://manned.org/dmidecode>.

- Muestra todos la tabla de contenidos de DMI:

`sudo dmidecode`

- Muestra la versión de la BIOS:

`sudo dmidecode {{[-s|--string]}} bios-version`

- Muestra el número de serie del equipo:

`sudo dmidecode {{[-s|--string]}} system-serial-number`

- Muestra información de la BIOS:

`sudo dmidecode {{[-t|--type]}} bios`

- Muestra información de la CPU:

`sudo dmidecode {{[-t|--type]}} processor`

- Muestra información de la memoria:

`sudo dmidecode {{[-t|--type]}} memory`
