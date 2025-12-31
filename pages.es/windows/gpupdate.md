# gpupdate

> Verifica y aplica la configuración de Directivas de Grupo de Windows.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/gpupdate>.

- Verifica y aplica la configuración de Directivas de Grupo actualizadas:

`gpupdate`

- Especifica la configuración de Directivas de Grupo objetivo para verificar actualizaciones:

`gpupdate /target:{{computadora|usuario}}`

- Fuerza a que se reapliquen todas las configuraciones de Directivas de Grupo:

`gpupdate /force`

- Muestra ayuda:

`gpupdate /?`
