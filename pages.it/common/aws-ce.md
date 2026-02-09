# aws ce

> Esegue operazioni di gestione dei costi tramite il servizio AWS Cost Explorer.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/ce/>.

- Crea monitor anomalie:

`aws ce create-anomaly-monitor --monitor {{nome_monitor}} --monitor-type {{tipo_monitor}}`

- Crea sottoscrizione anomalie:

`aws ce create-anomaly-subscription --subscription {{nome_subscription}} --monitor-arn {{arn_monitor}} --subscribers {{subscribers}}`

- Ottieni anomalie:

`aws ce get-anomalies --monitor-arn {{arn_monitor}} --start-time {{orario_inizio}} --end-time {{orario_fine}}`

- Ottieni costi e utilizzo:

`aws ce get-cost-and-usage --time-period {{data_inizio}}/{{data_fine}} --granularita' {{granularita'}} --metrics {{metriche}}`

- Ottieni previsione costi:

`aws ce get-cost-forecast --time-period {{data_inizio}}/{{data_fine}} --granularita' {{granularita'}} --metric {{metrica}}`

- Ottieni utilizzo prenotazioni:

`aws ce get-reservation-utilization --time-period {{data_inizio}}/{{data_fine}} --granularita' {{granularita'}}`

- Elenca definizioni categorie costi:

`aws ce list-cost-category-definitions`

- Aggiungi tag a risorsa:

`aws ce tag-resource --resource-arn {{arn_risorsa}} --tags {{tags}}`
