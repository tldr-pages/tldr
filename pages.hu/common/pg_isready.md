# pg_isready

> A PostgreSQL-kiszolgáló kapcsolatának állapotának ellenőrzése. További információ: <https://www.postgresql.org/docs/current/app-pg-isready.html>.

- Kapcsolat ellenőrzése:

`pg_isready`

- A kapcsolat ellenőrzése egy adott hostnévvel és porttal:

`pg_isready --host={{hostname}} --port={{port}}`

- Kapcsolat ellenőrzése: Csak akkor jelenít meg üzenetet, ha a kapcsolat sikertelen:

`pg_isready --quiet`
