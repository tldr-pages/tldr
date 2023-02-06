# tshark

> Csomagelemző eszköz, a Wireshark CLI változata. További információ: <https://tshark.dev/>.

- Figyeljen mindent a localhoston:

`tshark`

- Csak olyan csomagok rögzítése, amelyek megfelelnek egy adott rögzítési szűrőnek:

`tshark -f '{{udp port 53}}'`

- Csak egy adott kimeneti szűrőnek megfelelő csomagok megjelenítése:

`tshark -Y '{{http.request.method == "GET"}}'`

- Egy TCP-port dekódolása egy adott protokoll (pl. HTTP) segítségével:

`tshark -d tcp.port=={{8888}},{{http}}`

- A rögzített kimenet formátumának megadása:

`tshark -T {{json|text|ps|…}}`

- A kimenethez konkrét mezők kiválasztása:

`tshark -T {{fields|ek|json|pdml}} -e {{http.request.method}} -e {{ip.src}}`

- Rögzített csomag írása fájlba:

`tshark -w {{path/to/file}}`

- Csomagok elemzése fájlból:

`tshark -r {{path/to/file.pcap}}`
