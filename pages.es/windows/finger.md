# finger

> Devolver información sobre usuarios en un sistema especificado.
> El sistema remoto debe estar ejecutando el servicio Finger.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/finger>.

- Mostrar información sobre un usuario específico:

`finger {{usuario}}@{{host}}`

- Mostrar información sobre todos los usuarios en el host especificado:

`finger @{{host}}`

- Mostrar información en un formato más extenso:

`finger {{usuario}}@{{host}} -l`

- Mostrar información de ayuda:

`finger /?`
