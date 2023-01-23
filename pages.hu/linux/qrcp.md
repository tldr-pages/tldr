# qrcp

> Fájlátviteli eszköz. További információ: <https://github.com/claudiodangelis/qrcp>.

- Fájl vagy könyvtárak küldése:

`qrcp send {{path/to/file_or_directory path/to/file_directory ...}}`

- Fájlok fogadása:

`qrcp receive`

- Tartalom tömörítése az átvitel előtt:

`qrcp send --zip {{path/to/file_or_directory}}`

- Megadni egy használandó \[p\]ortot:

`qrcp {{send|receive}} --port {{port_number}}`

- A használandó hálózati \[i\]nterfész megadása:

`qrcp {{send|receive}} --interface interface`

- A kiszolgáló életben tartása:

`qrcp {{send|receive}} --keep-alive`
