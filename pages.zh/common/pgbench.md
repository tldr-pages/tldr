# pgbench

> 对 PostgreSQL 进行基准测试。
> 更多信息：<https://www.postgresql.org/docs/10/pgbench.html>。

- 使用默认大小的 50 倍的尺寸初始化数据库：

`pgbench --initialize --scale={{50}} {{database_name}}`

- 使用 10 个客户端、2 个工作线程和每个客户端 10,000 事务对数据库进行基准测试：

`pgbench --client={{10}} --jobs={{2}} --transactions={{10000}} {{database_name}}`
