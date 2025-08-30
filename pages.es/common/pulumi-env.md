# pulumi env

> Administra entornos Pulumi.
> Más información: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_env/>.

- Lista todos los entornos:

`pulumi env ls`

- Crea un entorno:

`pulumi env init {{nombre_entorno}}`

- Establece un valor en un entorno:

`pulumi env set {{nombre_entorno}} {{clave}} {{valor}}`

- Edita la definición de un entorno:

`pulumi env edit {{nombre_entorno}}`

- Elimina un valor de un entorno:

`pulumi env rm {{nombre_entorno}} {{clave}}`

- Elimina un entorno por completo:

`pulumi env rm {{nombre_entorno}}`

- Muestra la ayuda:

`pulumi env {{[-h|--help]}}`
