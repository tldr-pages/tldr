# dmidecode

> Mostra la taula de continguts del DMI (també conegut com SMBIOS) en un format llegible per humans.
> Requereix privilegis de root.
> Més informació: <https://manned.org/dmidecode>.

- Mostra tota la taula de continguts del DMI:

`sudo dmidecode`

- Mostra la versió de la BIOS:

`sudo dmidecode -s bios-version`

- Mostra el número de sèrie del equip:

`sudo dmidecode -s system-serial-number`

- Mostra informació de la BIOS:

`sudo dmidecode -t bios`

- Mostra informació de la CPU:

`sudo dmidecode -t processor`

- Mostra informació de la memòria:

`sudo dmidecode -t memory`
