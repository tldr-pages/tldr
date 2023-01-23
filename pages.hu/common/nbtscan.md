# nbtscan

> Hálózatok keresése NetBIOS névinformációk után. További információ: <https://github.com/resurrecting-open-source-projects/nbtscan>.

- Hálózat vizsgálata NetBIOS nevek után:

`nbtscan {{192.168.0.1/24}}`

- Egyetlen IP-cím beolvasása:

`nbtscan {{192.168.0.1}}`

- Szöveges kimenet megjelenítése:

`nbtscan -v {{192.168.0.1/24}}`

- Kimenet megjelenítése `/etc/hosts` formátumban:

`nbtscan -e {{192.168.0.1/24}}`

- IP-címek/hálózatok beolvasása egy fájlból:

`nbtscan -f {{path/to/file.txt}}`
