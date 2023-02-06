# cradle elastic

> Az Elasticsearch példányok kezelése egy Cradle-példányhoz. További információ: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#elastic>.

- Az Elasticsearch index csonkítása:

`cradle elastic flush`

- Az Elasticsearch index csonkítása egy adott csomaghoz:

`cradle elastic flush {{package_name}}`

- Az Elasticsearch séma beküldése:

`cradle elastic map`

- Az Elasticsearch séma elküldése egy adott csomaghoz:

`cradle elastic map {{package_name}}`

- Az Elasticsearch indexek feltöltése az összes csomaghoz:

`cradle elastic populate`

- Az Elasticsearch indexek feltöltése egy adott csomaghoz:

`cradle elastic populate {{package_name}}`
