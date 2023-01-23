# nvram

> A firmware változóinak kezelése. További információ: <https://ss64.com/osx/nvram.html>.

- \[p\]rint az NVRAM-ban tárolt összes változó:

`nvram -p`

- \[p\]rint az NVRAM-ban tárolt összes változó \[x\]ML formátummal:

`nvram -xp`

- A firmware-változó értékének módosítása:

`sudo nvram {{name}}="{{value}}"`

- \[d\]elete egy firmware-változót:

`sudo nvram -d {{name}}`

- \[c\]lear az összes firmware-változót:

`sudo nvram -c`

- Firmware-változó beállítása egy adott \[x\]ML \[f\]ile-ből:

`sudo nvram -xf {{path/to/file.xml}}`
