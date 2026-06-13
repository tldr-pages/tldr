# aws cur

> Crea, interroga ed elimina definizioni di report di utilizzo AWS.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/cur/>.

- Crea una definizione di report di costi e utilizzo AWS da un file JSON:

`aws cur put-report-definition --report-definition file://{{percorso/del/report_definition.json}}`

- Elenca le definizioni di report di utilizzo definite per l'account loggato:

`aws cur describe-report-definitions`

- Elimina una definizione di report di utilizzo:

`aws cur --region {{regione_aws}} delete-report-definition --report-name {{report}}`
