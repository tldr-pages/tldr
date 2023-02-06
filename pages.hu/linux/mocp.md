# mocp

> Music on Console (MOC) audio lejátszó. További információ: <https://manned.org/mocp>.

- Indítsa el a MOC terminál felhasználói felületét:

`mocp`

- A MOC terminál felhasználói felületének elindítása egy adott könyvtárban:

`mocp {{path/to/directory}}`

- A MOC-kiszolgáló elindítása a háttérben, a MOC terminál felhasználói felület elindítása nélkül:

`mocp --server`

- Egy adott dal hozzáadása a lejátszási sorba, miközben a MOC a háttérben van:

`mocp --enqueue {{path/to/audio_file}}`

- Dalok rekurzív hozzáadása a lejátszási sorba, miközben a MOC a háttérben van:

`mocp --append {{path/to/directory}}`

- A lejátszási sor törlése, miközben a MOC a háttérben van:

`mocp --clear`

- Az éppen sorban lévő dal lejátszása vagy leállítása, miközben a MOC a háttérben van:

`mocp --{{play|stop}}`

- A MOC-kiszolgáló leállítása, miközben a háttérben van:

`mocp --exit`
