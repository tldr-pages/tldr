# tofu fmt

> Formatea la configuración según las convenciones de estilo del lenguaje OpenTofu.
> Más información: <https://opentofu.org/docs/cli/commands/fmt/>.

- Formatea la configuración en el directorio actual:

`tofu fmt`

- Formatea la configuración en el directorio actual y subdirectorios:

`tofu fmt -recursive`

- Muestra los cambios de formato:

`tofu fmt -diff`

- No lista los ficheros formateados a `stdout`:

`tofu fmt -list=false`
