# elasticssearch-create-rerollment-token

> Ստեղծեք գրանցման նշաններ Elasticsearch հանգույցների և Kibana-ի օրինակների համար:.
> Լրացուցիչ տեղեկություններ. <https://www.elastic.co/docs/reference/elasticsearch/command-line-tools/create-enrollment-token>:.

- Ստեղծեք գրանցման նշան՝ նոր Elasticsearch հանգույց ավելացնելու համար.:

`elasticsearch-create-enrollment-token {{[-s|--scope]}} node`

- Ստեղծեք գրանցման նշան՝ Kibana-ի նոր օրինակ ավելացնելու համար.:

`elasticsearch-create-enrollment-token {{[-s|--scope]}} kibana`

- Ստեղծեք գրանցման նշան և ցուցադրեք մանրամասն արդյունքը.:

`elasticsearch-create-enrollment-token {{[-s|--scope]}} node --verbose`

- Ստեղծեք գրանցման նշան Kibana օրինակի համար հատուկ Elasticsearch URL-ով.:

`elasticsearch-create-enrollment-token {{[-s|--scope]}} kibana --url "{{ip}}"`

- Ցուցադրել օգնությունը.:

`elasticsearch-create-enrollment-token {{[-h|--help]}}`
