# pulumi state

> Edita el estado de la pila actual.
> Más información: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_state/>.

- Elimina un recurso del estado de la pila actual:

`pulumi state delete`

- Mueve un recurso de la pila actual a otra:

`pulumi state move {{recurso_urn}} --dest {{nombre_pila}}`

- Cambia el nombre de un recurso de la pila actual:

`pulumi state rename`

- Repara un estado no válido:

`pulumi state repair`

- Muestra la ayuda:

`pulumi state --help`
