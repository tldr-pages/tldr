# pulumi refresh

> Actualiza los recursos de una pila.
> Más información: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_refresh/>.

- Compara el estado de la pila actual con el estado en el proveedor de la nube y adopta cualquier cambio en la pila actual:

`pulumi refresh`

- Actualiza los recursos en la pila actual y muestra la operación como un diff enriquecido:

`pulumi refresh --diff`

- Actualiza los recursos de la pila actual y devuelve un error si se produce algún cambio durante la actualización:

`pulumi refresh --expect-no-changes`

- Solo muestra una vista previa de la actualización, pero no realiza la actualización en sí:

`pulumi refresh --preview-only`

- El nombre de la pila sobre la que operar (por defecto es la pila actual):

`pulumi refresh {{[-s|--stack]}} {{nombre_pila}}`

- Muestra la ayuda:

`pulumi refresh {{[-h|--help]}}`
