# pulumi destroy

> Elimina todos los recursos existentes en una pila.
> Más información: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_destroy/>.

- Elimina todos los recursos de la pila actual:

`pulumi destroy`

- Destruye todos los recursos de una pila específica:

`pulumi destroy {{[-s|--stack]}} {{stack}}`

- Acepta y destruye automáticamente los recursos tras la vista previa:

`pulumi destroy {{[-y|--yes]}}`

- Excluye los recursos protegidos de la destrucción:

`pulumi destroy --exclude-protected`

- Elimina la pila y su archivo de configuración después de que se hayan eliminado todos los recursos de la pila:

`pulumi destroy --remove`

- Continua con la destrucción de los recursos, incluso si se produce un error:

`pulumi destroy --continue-on-error`
