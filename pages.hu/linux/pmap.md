# pmap

> Egy folyamat vagy folyamatok memóriatérképének jelentése. További információ: <https://manned.org/pmap>.

- Memóriatérkép nyomtatása egy adott folyamatazonosítóhoz (PID):

`pmap {{pid}}`

- Megjeleníti a kiterjesztett formátumot:

`pmap --extended {{pid}}`

- Az eszköz formátumának megjelenítése:

`pmap --device {{pid}}`

- Az eredmények korlátozása a `low` és a `high` által meghatározott memóriacím-tartományra:

`pmap --range {{low}},{{high}}`

- Több folyamat memóriatérképének nyomtatása:

`pmap {{pid1 pid2 ...}}`
