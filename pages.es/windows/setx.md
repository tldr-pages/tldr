# setx

> Establece variables de entorno persistentes.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/setx>.

- Establecer una variable de entorno para el usuario actual:

`setx {{variable}} {{valor}}`

- Establecer una variable de entorno para la máquina actual:

`setx {{variable}} {{valor}} /M`

- Establecer una variable de entorno para un usuario en una máquina remota:

`setx /s {{hostname}} /u {{username}} /p {{password}} {{variable}} {{valor}}`

- Establecer una variable de entorno desde el valor de una clave de registro:

`setx {{variable}} /k {{registro\ruta\clave}}`
