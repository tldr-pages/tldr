# aws cur

> Crea, solicita y elimina definiciones de informes de uso de AWS.
> Más información: <https://docs.aws.amazon.com/cli/latest/reference/cur/>.

- Crea una definición de informe de costes y uso de AWS a partir de un archivo JSON:

`aws cur put-report-definition --report-definition file://{{ruta/al/report_definition.json}}`

- Enumera las definiciones de informes de uso definidas para la cuenta conectada:

`aws cur describe-report-definitions`

- Elimina una definición de informe de uso:

`aws cur --region {{aws_region}} delete-report-definition --report-name {{report}}`
