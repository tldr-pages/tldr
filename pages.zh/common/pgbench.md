# pgbench

> 在PostgreSQL上运行基准测试。
> 更多信息：<https://www.postgresql.org/docs/10/pgbench.html>。

- 使用默认大小的50倍规模因子初始化数据库：

`pgbench --initialize --scale={{50}} {{database_name}}`

- 使用10个客户端、2个工作线程和每个客户端10,000个事务对数据库进行基准测试：

`pgbench --client={{10}} --jobs={{2}} --transactions={{10000}} {{database_name}}`