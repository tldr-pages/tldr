# pulumi org

> Gestiona la configuración de la organización Pulumi.
> Más información: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_org/>.

- Muestra la organización predeterminada y el backend actual:

`pulumi org`

- Muestra la organización predeterminada:

`pulumi org get-default`

- Establece la organización predeterminada:

`pulumi org set-default {{nombre_de_la_organización}}`

- Busca recursos en Pulumi Cloud utilizando Pulumi AI con una consulta en lenguaje natural de texto sin formato:

`pulumi org search ai {{[-q|--query]}} {{«muéstrame todos los equilibradores de carga de mi organización»}}`

- Muestra la ayuda:

`pulumi org {{[-h|--help]}}`
