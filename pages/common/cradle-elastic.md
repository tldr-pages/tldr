# cradle elastic

> Manage the Elasticsearch instances for a Cradle instance.
> More information: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#elastic>.

- Truncate the Elasticsearch index:

`cradle elastic flush`

- Truncate the Elasticsearch index for a specific package:

`cradle elastic flush {{package_name}}`

- Submit the Elasticsearch schema:

`cradle elastic map`

- Submit the Elasticsearch schema for a specific package:

`cradle elastic map {{package_name}}`

- Populate the Elasticsearch indices for all packages:

`cradle elastic populate`

- Populate the Elasticsearch indices for a specific package:

`cradle elastic populate {{package_name}}`
