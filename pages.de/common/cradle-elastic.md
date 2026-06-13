# cradle elastic

> Verwalte ElasticSearch Instanzen einer Cradle Instanz.
> Weitere Informationen: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#elastic>.

- Entleere den ElasticSearch Index:

`cradle elastic flush`

- Entleere den ElasticSearch Index für ein bestimmtes Paket:

`cradle elastic flush {{paket}}`

- Sende ein ElasticSearch Schema ab:

`cradle elastic map`

- Sende ein ElasticSearch Schema für ein bestimmtes Paket ab:

`cradle elastic map {{paket}}`

- Befülle die ElasticSearch Indizes für alle Pakete:

`cradle elastic populate`

- Befülle die ElasticSearch Indizes für ein bestimmtes Paket:

`cradle elastic populate {{paket}}`
