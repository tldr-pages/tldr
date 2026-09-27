# setx

> Establece variables de entorno persistentes.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/setx>.

- Establece una variable de entorno para el usuario actual:

`setx {{variable}} {{valor}}`

- Establece una variable de entorno para la máquina actual:

`setx {{variable}} {{valor}} /M`

- Establece una variable de entorno para un usuario en una máquina remota:

`setx /s {{hostname}} /u {{username}} /p {{password}} {{variable}} {{valor}}`

- Establece una variable de entorno desde el valor de una clave de registro:

`setx {{variable}} /k {{registro\ruta\clave}}`
