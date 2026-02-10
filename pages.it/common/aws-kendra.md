# aws kendra

> CLI per AWS Kendra.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/kendra/>.

- Crea un indice:

`aws kendra create-index --name {{nome}} --role-arn {{arn_ruolo}}`

- Elenca gli indici:

`aws kendra list-indexes`

- Descrivi un indice:

`aws kendra describe-index --id {{id_indice}}`

- Elenca le fonti dati:

`aws kendra list-data-sources`

- Descrivi una fonte dati:

`aws kendra describe-data-source --id {{id_sorgente_dati}}`

- Elenca i suggerimenti di query di ricerca:

`aws kendra list-query-suggestions --index-id {{id_indice}} --query-text {{testo_query}}`
