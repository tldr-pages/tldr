# terraform output

> Exporta datos estructurados sobre tus recursos Terraform.
> Más información: <https://developer.hashicorp.com/terraform/cli/commands/output>.

- Sin argumentos adicionales, `output` mostrará todas las salidas del módulo raíz:

`terraform output`

- Genera solo un valor con un nombre específico:

`terraform output {{nombre}}`

- Convierte el valor de salida en una cadena sin formato (útil para scripts de shell):

`terraform output -raw`

- Formatea las salidas como un objeto JSON, con una clave por cada salida (útil con jq):

`terraform output -json`
