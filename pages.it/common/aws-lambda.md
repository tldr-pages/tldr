# aws lambda

> Utilizza AWS Lambda, un servizio di calcolo per eseguire codice senza provisionare o gestire server.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/lambda/>.

- Esegui una funzione:

`aws lambda invoke --function-name {{nome}} {{percorso/del/response.json}}`

- Esegui una funzione con un payload di input in formato JSON:

`aws lambda invoke --function-name {{nome}} --payload {{json}} {{percorso/del/response.json}}`

- Elenca le funzioni:

`aws lambda list-functions`

- Visualizza la configurazione di una funzione:

`aws lambda get-function-configuration --function-name {{nome}}`

- Elenca gli alias delle funzioni:

`aws lambda list-aliases --function-name {{nome}}`

- Visualizza la configurazione di concorrenza riservata per una funzione:

`aws lambda get-function-concurrency --function-name {{nome}}`

- Elenca quali servizi AWS possono invocare la funzione:

`aws lambda get-policy --function-name {{nome}}`
