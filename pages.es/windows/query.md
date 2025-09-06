# query

> Mostrar información sobre sesiones de usuario y procesos.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/query>.

- Mostrar todas las sesiones de usuario:

`query session`

- Mostrar las sesiones de usuario actuales en un equipo remoto:

`query session /server:{{nombre_del_servidor}}`

- Mostrar usuarios conectados:

`query user`

- Mostrar todas las sesiones de usuario en un equipo remoto:

`query session /server:{{nombre_del_servidor}}`

- Mostrar todos los procesos en ejecución:

`query process`

- Mostrar procesos en ejecución por nombre de sesión o nombre de usuario:

`query process {{nombre_de_sesion|nombre_de_usuario}}`
