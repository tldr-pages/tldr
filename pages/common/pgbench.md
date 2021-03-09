# pgbench

> pgbench — run a benchmark test on PostgreSQL
> More information: <https://www.postgresql.org/docs/10/pgbench.html>.

- Initialize database example with scaling option of 50 times the default size:

`pgbench -i -s 50 example`

- Benchmark with 10 clients, 2 worker threads, and 10,000 transactions per client:

`pgbench -c 10 -j 2 -t 10000 example`
