# aws pricing

> Consulta servicios, productos e información de precios de Amazon Web Services.
> Más información: <https://docs.aws.amazon.com/cli/latest/reference/pricing/>.

- Lista códigos de servicio de una región específica:

`aws pricing describe-services --region {{us-east-1}}`

- Lista atributos para un código de servicio dado en una región específica:

`aws pricing describe-services --service-code {{AmazonEC2}} --region {{us-east-1}}`

- Imprime información de precios para un código de servicio en una región específica:

`aws pricing get-products --service-code {{AmazonEC2}} --region {{us-east-1}}`

- Lista valores para un atributo específico para un código de servicio en una región específica:

`aws pricing get-attribute-values --service-code {{AmazonEC2}} --attribute-name {{instanceType}} --region {{us-east-1}}`

- Imprime información de precios para un código de servicio usando filtros por tipo de instancia y ubicación:

`aws pricing get-products --service-code {{AmazonEC2}} --filters "{{Type=TERM_MATCH,Field=instanceType,Value=m5.xlarge}}" "{{Type=TERM_MATCH,Field=location,Value=US East (N. Virginia)}}" --region {{us-east-1}}`
