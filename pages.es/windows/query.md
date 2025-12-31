# query

> Muestra información sobre sesiones de usuario y procesos.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/query>.

- Muestra todas las sesiones de usuario:

`query session`

- Muestra las sesiones de usuario actuales en un equipo remoto:

`query session /server:{{nombre_del_servidor}}`

- Muestra usuarios conectados:

`query user`

- Muestra todas las sesiones de usuario en un equipo remoto:

`query session /server:{{nombre_del_servidor}}`

- Muestra todos los procesos en ejecución:

`query process`

- Muestra procesos en ejecución por nombre de sesión o nombre de usuario:

`query process {{nombre_de_sesion|nombre_de_usuario}}`
