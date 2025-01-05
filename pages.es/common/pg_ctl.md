# pg_ctl

> Utilidad para controlar un servidor PostgreSQL y un grupo (clúster) de bases de datos.
> Más información: <https://www.postgresql.org/docs/current/app-pg-ctl.html>.

- Inicia un nuevo grupo de base de datos PostgreSQL:

`pg_ctl -D {{directorio_de_datos}} init`

- Inicia un servidor PostgreSQL:

`pg_ctl -D {{directorio_de_datos}} start`

- Detiene un servidor PostgreSQL:

`pg_ctl -D {{directorio_de_datos}} stop`

- Reinicia un servidor PostgreSQL:

`pg_ctl -D {{directorio_de_datos}} restart`

- Recarga la configuración del servidor PostgreSQL:

`pg_ctl -D {{directorio_de_datos}} reload`
