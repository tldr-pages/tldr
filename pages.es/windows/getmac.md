# getmac

> Muestra las direcciones MAC de un sistema.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/getmac>.

- Muestra las direcciones MAC del sistema actual:

`getmac`

- Muestra los detalles en un formato específico:

`getmac /fo {{table|list|csv}}`

- Excluye la cabecera en la lista de salida:

`getmac /nh`

- Muestra las direcciones MAC de un equipo remoto:

`getmac /s {{nombre_host}} /u {{nombredeusuario}} /p {{contraseña}}`

- Muestra las direcciones MAC con información detallada:

`getmac /v`

- Muestra información de uso detallada:

`getmac /?`
