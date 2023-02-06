# pyrit

> WPA/WPA2 feltörő eszköz, amely számítási teljesítményt használ. További információ: <https://github.com/JPaulMora/Pyrit>.

- A rendszer feltörési sebességének megjelenítése:

`pyrit benchmark`

- A rendelkezésre álló magok listája:

`pyrit list_cores`

- \[e\]SSID beállítása:

`pyrit -e "{{ESSID}}" create_essid`

- \[r\]eading and analyze a specific packet capture file:

`pyrit -r {{path/to/file.cap|path/to/file.pcap}} analyze`

- Jelszavak olvasása és \[i\]mportálása az aktuális adatbázisba:

`pyrit -i {{path/to/file}} {{import_unique_passwords|unique_passwords|import_passwords}}`

- Jelszavak kiterjesztése az adatbázisból egy adott fájlba:

`pyrit -o {{path/to/file}} export_passwords`

- Jelszavak lefordítása Pired Master Keys segítségével:

`pyrit batch`

- \[r\]eading the capture file and crack the password:

`pyrit -r {{path/to/file}} attack_db`
