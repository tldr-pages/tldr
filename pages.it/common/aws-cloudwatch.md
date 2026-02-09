# aws cloudwatch

> Monitora le risorse AWS per ottenere visibilità a livello di sistema sull'utilizzo delle risorse, le prestazioni delle applicazioni e la salute operativa.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/>.

- Elenca le dashboard per il tuo account:

`aws cloudwatch list-dashboards`

- Visualizza i dettagli per la dashboard specificata:

`aws cloudwatch get-dashboard --dashboard-name {{nome_dashboard}}`

- Elenca le metriche:

`aws cloudwatch list-metrics`

- Elenca gli allarmi:

`aws cloudwatch describe-alarms`

- Crea o aggiorna un allarme e lo associa a una metrica:

`aws cloudwatch put-metric-alarm --alarm-name {{nome_allarme}} --evaluation-periods {{evaluation_periods}} --comparison-operator {{comparison_operator}}`

- Elimina gli allarmi specificati:

`aws cloudwatch delete-alarms --alarm-names {{nomi_allarme}}`

- Elimina le dashboard specificate:

`aws cloudwatch delete-dashboards --dashboard-names {{nome_dashboard}}`
