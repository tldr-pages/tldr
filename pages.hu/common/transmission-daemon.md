# transmission-daemon

> A démon a `transmission-remote` vagy annak webes felületével vezérelhető. Lásd még: `transmission`. További információ: <https://manned.org/transmission-daemon>.

- A `transmission` fej nélküli munkamenet indítása:

`transmission-daemon`

- Egy adott könyvtár indítása és figyelése új torrentek után:

`transmission-daemon --watch-dir {{path/to/directory}}`

- A démon beállításainak kidobása JSON formátumban:

`transmission-daemon --dump-settings > {{path/to/file.json}}`

- Indítás a webes felület meghatározott beállításaival:

`transmission-daemon --auth --username {{username}} --password {{password}} --port {{9091}} --allowed {{127.0.0.1}}`
