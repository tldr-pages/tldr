# pulumi up

> Crea o actualiza los recursos de una pila.
> Más información: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_up/>.

- Previsualiza e implementa los cambios en un programa y/o en la infraestructura:

`pulumi up`

- Aprueba y realiza automáticamente la actualización tras previsualizarla:

`pulumi up {{[-y|--yes]}}`

- Previsualiza e implementa cambios en una pila específica:

`pulumi up {{[-s|--stack]}} {{pila}}`

- Actualiza el estado de los recursos de la pila antes de actualizar:

`pulumi up {{[-r|--refresh]}}`

- No muestra los resultados de la pila:

`pulumi up --suppress-outputs`

- Continua actualizando los recursos, incluso si se produce un error:

`pulumi up --continue-on-error`

- Muestra la ayuda:

`pulumi up {{[-h|--help]}}`
