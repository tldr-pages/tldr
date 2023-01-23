# dmidecode

> A DMI (más néven SMBIOS) táblázat tartalmának megjelenítése ember által olvasható formátumban. Root jogosultságokat igényel. További információ: <https://manned.org/dmidecode>.

- Az összes DMI-tábla tartalmának megjelenítése:

`sudo dmidecode`

- A BIOS verziójának megjelenítése:

`sudo dmidecode -s bios-version`

- A rendszer sorozatszámának megjelenítése:

`sudo dmidecode -s system-serial-number`

- BIOS-információk megjelenítése:

`sudo dmidecode -t bios`

- CPU-információk megjelenítése:

`sudo dmidecode -t processor`

- Memóriainformációk megjelenítése:

`sudo dmidecode -t memory`
