# groupadd

> Añade grupos de usuarios al sistema.
> Vea también: `groups`, `groupdel`, `groupmod`.
> Más información: <https://manned.org/groupadd>.

- Crea un nuevo grupo:

`sudo groupadd {{nombre_del_grupo}}`

- Cree un nuevo grupo del sistema:

`sudo groupadd {{[-r|--system]}} {{nombre_del_grupo}}`

- Crea un nuevo grupo con el identificador de grupo específico:

`sudo groupadd {{[-g|--gid]}} {{id}} {{nombre_del_grupo}}`
