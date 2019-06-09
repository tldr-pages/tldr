# cradle elastic

> Gestisci le istanze ElasticSearch per un'istanza Cradle.
> Maggiori informazioni: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#elastic>.

- Svuota l'indice ElasticSearch:

`cradle elastic flush`

- Svuota l'indice ElasticSearch per uno specifico pacchetto:

`cradle elastic flush {{nome_pacchetto}}`

- Carica lo schema ElasticSearch:

`cradle elastic map`

- Carica lo schema ElasticSearch per uno specifico pacchetto:

`cradle elastic map {{nome_pacchetto}}`

- Popola gli indici ElasticSearch per tutti i pacchetti:

`cradle elastic populate`

- Popola gli indici ElasticSearch per uno specifico pacchetto:

`cradle elastic populate {{nome_pacchetto}}`
