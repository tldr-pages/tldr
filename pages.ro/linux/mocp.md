# mocp

> Music on consolă (MOC) player audio.
> Mai multe informaţii: <https://manned.org/mocp>

- Lansarea terminalului MOC UI:

`mocp`

- Lansarea terminalului MOC UI într-un anumit director:

`mocp {{path/to/directory}}`

- Porniți serverul MOC în fundal, fără a lansa UI terminalul MOC:

`mocp --server`

- Adăugați o anumită melodie la coada de redare în timp ce MOC este în fundal:

`mocp --enqueue {{path/to/audio_file}}`

- Adăugați melodii recursiv la coada de redare în timp ce MOC este în fundal:

`mocp --append {{path/to/directory}}`

- Ștergeți coada de redare în timp ce MOC este în fundal:

`mocp --clear`

- Redați sau opriți melodia momentan în coadă în timp ce MOC se află în fundal:

`mocp --{{play|stop}}`

- Opriți serverul MOC în timp ce este în fundal:

`mocp --exit`
