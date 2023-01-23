# df

> Áttekintést ad a fájlrendszer lemezterületének felhasználásáról. További információ: <https://www.gnu.org/software/coreutils/df>.

- Megjeleníti az összes fájlrendszert és azok lemezhasználatát:

`df`

- Megjeleníti az összes fájlrendszert és azok lemezhasználatát ember által olvasható formában:

`df -h`

- Az adott fájlt vagy könyvtárat tartalmazó fájlrendszer és lemezhasználatának megjelenítése:

`df {{path/to/file_or_directory}}`

- A szabad inode-ok számával kapcsolatos statisztikák megjelenítése:

`df -i`

- A fájlrendszerek megjelenítése, de a megadott típusok kizárása:

`df -x {{squashfs}} -x {{tmpfs}}`
