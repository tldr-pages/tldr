# dmidecode

> Afișați conținutul tabelului DMI (cunoscut ca SMBIOS) într-un format care poate fi citit de om.
> Necesită privilegii de root.
> Mai multe informaţii: <https://manned.org/dmidecode>

- Afișează tot conținutul tabelului DMI:

`sudo dmidecode`

- Afișați versiunea BIOS:

`sudo dmidecode -s bios-version`

- Arată numărul de serie al sistemului:

`sudo dmidecode -s system-serial-number`

- Afișează informații BIOS:

`sudo dmidecode -t bios`

- Afișează informații CPU:

`sudo dmidecode -t processor`

- Afișează informații despre memorie:

`sudo dmidecode -t memory`
