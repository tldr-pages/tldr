# aws kendra

> CLI para AWS Kendra.
> Más información: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/index.html>.

- Crea un índice:

`aws kendra create-index --name {{nombre}} --role-arn {{rol_arn}}`

- Lista índices:

`aws kendra list-indexes`

- Describe un índice:

`aws kendra describe-index --id {{id_índice}}`

- Lista fuentes de datos:

`aws kendra list-data-sources`

- Describe una fuente de datos:

`aws kendra describe-data-source --id {{id_fuente_datos}}`

- Lista consultas de búsqueda:

`aws kendra list-query-suggestions --index-id {{id_índice}} --query-text {{texto_consulta}}`
