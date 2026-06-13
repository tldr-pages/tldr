# aws glue

> CLI para AWS Glue.
> Define el punto de enlace público para el servicio AWS Glue.
> Más información: <https://docs.aws.amazon.com/cli/latest/reference/glue/>.

- Lista trabajos:

`aws glue list-jobs`

- Inicia un trabajo:

`aws glue start-job-run --job-name {{nombre_del_trabajo}}`

- Inicia la ejecución de un flujo de trabajo:

`aws glue start-workflow-run --name {{nombre_del_flujo}}`

- Lista disparadores:

`aws glue list-triggers`

- Inicia un disparador:

`aws glue start-trigger --name {{nombre_disparador}}`

- Crea un punto final de desarrollo:

`aws glue create-dev-endpoint --endpoint-name {{nombre}} --role-arn {{role_arn_usado_por_puntofinal}}`
