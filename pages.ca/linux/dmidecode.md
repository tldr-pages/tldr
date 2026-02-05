# dmidecode

> Mostra la taula de continguts del DMI (també conegut com SMBIOS) en un format llegible per humans.
> Requereix privilegis de root.
> Més informació: <https://manned.org/dmidecode>.

- Mostra tota la taula de continguts del DMI:

`sudo dmidecode`

- Mostra la versió de la BIOS:

`sudo dmidecode {{[-s|--string]}} bios-version`

- Mostra el número de sèrie del equip:

`sudo dmidecode {{[-s|--string]}} system-serial-number`

- Mostra informació de la BIOS:

`sudo dmidecode {{[-t|--type]}} bios`

- Mostra informació de la CPU:

`sudo dmidecode {{[-t|--type]}} processor`

- Mostra informació de la memòria:

`sudo dmidecode {{[-t|--type]}} memory`
