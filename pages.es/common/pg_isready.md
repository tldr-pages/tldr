# pg_isready

> Comprueba el estado de conexión de un servidor PostgreSQL.
> Más información: <https://www.postgresql.org/docs/current/app-pg-isready.html>.

- Verifica la conexión:

`pg_isready`

- Revisa la conexión con un nombre de host específico y el puerto:

`pg_isready --host={{nombre_del_equipo}} --port={{puerto}}`

- Comprueba la conexión mostrando un mensaje solo cuando la conexión falla:

`pg_isready --quiet`
