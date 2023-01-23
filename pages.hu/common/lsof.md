# lsof

> A megnyitott fájlok és a hozzájuk tartozó folyamatok listázása. Megjegyzés: A mások által megnyitott fájlok listázásához gyökérjogok (vagy sudo) szükségesek. További információ: <https://manned.org/lsof>.

- Megkeresi azokat a folyamatokat, amelyekben egy adott fájl nyitva van:

`lsof {{path/to/file}}`

- Keresse meg azt a folyamatot, amelyik megnyitott egy helyi internetes portot:

`lsof -i :{{port}}`

- Csak a folyamat azonosítóját (PID) adja ki:

`lsof -t {{path/to/file}}`

- Az adott felhasználó által megnyitott fájlok listázása:

`lsof -u {{username}}`

- Az adott parancs vagy folyamat által megnyitott fájlok listázása:

`lsof -c {{process_or_command_name}}`

- Egy adott folyamat által megnyitott fájlok listázása, a PID azonosítója alapján:

`lsof -p {{PID}}`

- Megnyitott fájlok listázása egy könyvtárban:

`lsof +D {{path/to/directory}}`

- Keresse meg a helyi IPv6 TCP porton figyelő folyamatot, és ne konvertálja a hálózati vagy port számokat:

`lsof -i6TCP:{{port}} -sTCP:LISTEN -n -P`
