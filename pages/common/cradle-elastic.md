# cradle elastic

> Manage the ElasticSearch instances for a Cradle instance.

- Truncate the ElasticSearch index:

`cradle elastic flush`

- Truncate the ElasticSearch index for a specific package:

`cradle elastic flush {{package}}`

- Submit the ElasticSearch schema:

`cradle elastic map`

- Submit the ElasticSearch schema for a specific package:

`cradle elastic map {{package}}`

- Populate the ElasticSearch indexes for all packages:

`cradle elastic populate`

- Populate the ElasticSearch indexes for a specific package:

`cradle elastic populate {{package}}`
