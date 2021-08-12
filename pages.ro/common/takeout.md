# takeout

> Un manager de dependenţă bazat pe Docker.
> Mai multe informaţii: <https://github.com/tighten/takeout>

- Afișați o listă de servicii disponibile:

`takeout enable`

- Activați un anumit serviciu:

`takeout enable {{name}}`

- Activați un anumit serviciu cu parametrii impliciți:

`takeout enable --default {{name}}`

- Afișează o listă de servicii activate:

`takeout disable`

- Dezactivați un anumit serviciu:

`takeout disable {{name}}`

- Dezactivați toate serviciile:

`takeout disable --all`

- Porniți un container specific:

`takeout start {{container_id}}`

- Opriți un container specific:

`takeout stop {{container_id}}`
