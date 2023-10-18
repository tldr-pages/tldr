# aws cur

> Crea, solicita y elimina definiciones de informes de uso de AWS.
> Más información: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cur/index.html>.

- Crea una definición de informe de costes y uso de AWS a partir de un archivo JSON:

`aws cur put-report-definition --report-definition file://{{ruta/al/report_definition.json}}`

- Enumera las definiciones de informes de uso definidas para la cuenta conectada:

`aws cur describe-report-definitions`

- Elimina una definición de informe de uso:

`aws cur --region {{aws_region}} delete-report-definition --report-name {{report}}`
