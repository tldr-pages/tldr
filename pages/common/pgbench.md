# pgbench

> Run a benchmark test on PostgreSQL.
> More information: <https://www.postgresql.org/docs/10/pgbench.html>.

- Initialize database example with scaling option of 50 times the default size:

`pgbench --initialize --scale={{50}} {{database_name}}`

- Benchmark with 10 clients, 2 worker threads, and 10,000 transactions per client:

`pgbench --clients={{10}} --jobs={{2}} --transactions={{10000}} {{database_name}}`
