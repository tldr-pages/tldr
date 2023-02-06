# ledctl

> Intel(R) Enclosure LED Control Application. További információ: <https://manned.org/ledctl>.

- Kapcsolja be a "Locate" LED-et a megadott eszköz(ök) esetében:

`sudo ledctl locate={{/dev/sda,/dev/sdb,...}}`

- A "Locate" LED kikapcsolása a megadott eszköz(ök) esetében:

`sudo ledctl locate_off={{/dev/sda,/dev/sdb,...}}`

- Az "Status" LED és a "Failure" LED kikapcsolása a megadott eszköz(ök)nél:

`sudo ledctl off={{/dev/sda,/dev/sdb,...}}`

- Kikapcsolja az "Állapot" LED-et, a "Hiba" LED-et és a "Helymeghatározás" LED-et a megadott eszköz(ök)nél:

`sudo ledctl normal={{/dev/sda,/dev/sdb,...}}`
