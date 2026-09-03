# pgbench

> Run a benchmark test on PostgreSQL.
> More information: <https://www.postgresql.org/docs/current/pgbench.html>.

- Initialize a database with a scale factor of 50 times the default size:

`pgbench {{database_name}} {{[-i|--initialize]}} {{[-s|--scale]}} {{50}}`

- Benchmark a database with 10 clients, 2 worker threads, and 10,000 transactions per client:

`pgbench {{database_name}} {{[-c|--client]}} {{10}} {{[-j|--jobs]}} {{2}} {{[-t|--transactions]}} {{10000}}`
