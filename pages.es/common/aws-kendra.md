# aws kendra

> CLI para AWS Kendra.
> Más información: <https://docs.aws.amazon.com/cli/latest/reference/kendra/index.html>.

- Crea un índice:

`aws kendra create-index --name {{nombre}} --role-arn {{rol-arn}}`

- Lista índices:

`aws kendra list-indexes`

- Describe un índice:

`aws kendra describe-index --id {{id-indice}}`

- Lista fuentes de datos:

`aws kendra list-data-sources`

- Describe una fuente de datos:

`aws kendra describe-data-source --id {{id-fuente-datos}}`

- Lista consultas de búsqueda:

`aws kendra list-query-suggestions --index-id {{id-indice}} --query-text {{texto-consulta}}`
