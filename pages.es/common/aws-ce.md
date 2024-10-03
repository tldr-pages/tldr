# aws ce

> Ejecuta operaciones de gestión de costos a través del servicio AWS Cost Explorer.
> Más información: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/index.html>.

- Crea monitor de anomalías:

`aws ce create-anomaly-monitor --monitor {{nombre_monitor}} --monitor-type {{tipo_monitor}}`

- Crea suscripción de anomalías:

`aws ce create-anomaly-subscription --subscription {{nombre_de_suscripción}} --monitor-arn {{monitor_arn}} --subscribers {{suscriptores}}`

- Obtiene anomalías:

`aws ce get-anomalies --monitor-arn {{monitor_arn}} --start-time {{hora_de_inicio}} --end-time {{hora_final}}`

- Obtiene coste y uso:

`aws ce get-cost-and-usage --time-period {{fecha_inicio}}/{{fecha_final}} --granularity {{granularidad}} --metrics {{métricas}}`

- Obtiene previsión de costes:

`aws ce get-cost-forecast --time-period {{fecha_inicio}}/{{fecha_final}} --granularity {{granularidad}} --metric {{métrica}}`

- Obtiene la utilización de la reserva:

`aws ce get-reservation-utilization --time-period {{fecha_inicio}}/{{fecha_final}} --granularity {{granularidad}}`

- Lista de definiciones de categorías de costes:

`aws ce list-cost-category-definitions`

- Recurso de etiquetas:

`aws ce tag-resource --resource-arn {{recurso_arn}} --tags {{etiquetas}}`
