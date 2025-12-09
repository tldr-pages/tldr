# tofu output

> Exporta datos estructurados sobre tus recursos OpenTofu.
> Más información: <https://opentofu.org/docs/cli/commands/output/>.

- Sin argumentos adicionales, `output` mostrará todas las salidas del módulo raíz:

`tofu output`

- Muestra solo un valor con un nombre específico:

`tofu output {{nombre}}`

- Convierte el valor de salida en una cadena sin procesar (útil para un conjunto de instrucciones de la consola):

`tofu output -raw`

- Formatea las salidas como un objeto JSON, con una clave por salida (útil con `jq`):

`tofu output -json`
