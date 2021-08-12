# pgbench

> Rulați un test de referință pe PostgreSQL.
> Mai multe informaţii: <https://www.postgresql.org/docs/10/pgbench.html>

- Inițializarea unei baze de date cu un factor de scală de 50 de ori dimensiunea implicită:

`pgbench --initialize --scale={{50}} {{database_name}}`

- Benchmark o bază de date cu 10 clienți, 2 fire de lucrător și 10.000 de tranzacții per client:

`pgbench --client={{10}} --jobs={{2}} --transactions={{10000}} {{database_name}}`
