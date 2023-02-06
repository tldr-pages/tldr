# rsstail

> `tail` az RSS feedek esetében. További információ: <https://github.com/gvalkov/rsstail.py>.

- Megjeleníti egy adott URL-cím feedjét, és várja az alján megjelenő új bejegyzések megjelenését:

`rsstail -u {{url}}`

- A feed fordított időrendi sorrendben történő megjelenítése (az újabbak alul):

`rsstail -r -u {{url}}`

- A közzététel dátumának és a linknek a feltüntetése:

`rsstail -pl -u {{url}}`

- Frissítési időköz beállítása:

`rsstail -u {{url}} -i {{interval_in_seconds}}`

- Feed megjelenítése és kilépés:

`rsstail -1 -u {{url}}`
