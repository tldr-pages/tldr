# daemon

> Folyamatok futtatása démonokká. További információ: <https://manned.org/man/daemon.1>.

- Parancs futtatása démonként:

`daemon --name="{{name}}" {{command}}`

- Futtasson egy parancsot démonként, amely újraindul, ha a parancs összeomlik:

`daemon --name="{{name}}" --respawn {{command}}`

- Futtasson egy parancsot démonként, amely újraindul, ha a parancs összeomlik, 10 másodpercenként két próbálkozással:

`daemon --name="{{name}}" --respawn --attempts=2 --delay=10 {{command}}`

- Parancs futtatása démonként, naplófájlok írása egy adott fájlba:

`daemon --name="{{name}}" --errlog={{path/to/file.log}} {{command}}`

- Egy démon leállítása (SIGTERM):

`daemon --name="{{name}}" --stop`

- A démonok listázása:

`daemon --list`
