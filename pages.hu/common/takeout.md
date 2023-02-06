# takeout

> Docker-alapú, kizárólag fejlesztői függőségkezelő. További információ: <https://github.com/tighten/takeout>.

- Az elérhető szolgáltatások listájának megjelenítése:

`takeout enable`

- Egy adott szolgáltatás engedélyezése:

`takeout enable {{name}}`

- Egy adott szolgáltatás engedélyezése az alapértelmezett paraméterekkel:

`takeout enable --default {{name}}`

- Az engedélyezett szolgáltatások listájának megjelenítése:

`takeout disable`

- Egy adott szolgáltatás letiltása:

`takeout disable {{name}}`

- Az összes szolgáltatás letiltása:

`takeout disable --all`

- Egy adott konténer indítása:

`takeout start {{container_id}}`

- Egy adott konténer leállítása:

`takeout stop {{container_id}}`
