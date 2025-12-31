# finger

> Devuelve información sobre usuarios en un sistema especificado.
> El sistema remoto debe estar ejecutando el servicio Finger.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/finger>.

- Muestra información sobre un usuario específico:

`finger {{usuario}}@{{host}}`

- Muestra información sobre todos los usuarios en el host especificado:

`finger @{{host}}`

- Muestra información en un formato más extenso:

`finger {{usuario}}@{{host}} -l`

- Muestra información de ayuda:

`finger /?`
