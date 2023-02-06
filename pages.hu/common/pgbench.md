# pgbench

> Benchmark teszt futtatása a PostgreSQL-en. További információ: <https://www.postgresql.org/docs/10/pgbench.html>.

- Inicializáljon egy adatbázist az alapértelmezett méret 50-szeresének méretezési tényezőjével:

`pgbench --initialize --scale={{50}} {{database_name}}`

- Vizsgáljon meg egy adatbázist 10 ügyféllel, 2 munkaszállal és ügyfelenként 10 000 tranzakcióval:

`pgbench --client={{10}} --jobs={{2}} --transactions={{10000}} {{database_name}}`
