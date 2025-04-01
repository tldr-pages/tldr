# odps table

> 在 ODPS (开放数据处理服务) 中创建和修改表。
> 更多信息：<https://www.alibabacloud.com/help/doc-detail/27971.htm>。
> 参见 `odps`。

- 创建带分区和生命周期的表：

`create table {{table_name}} ({{col}} {{type}}) partitioned by ({{col}} {{type}}) lifecycle {{days}};`

- 基于另一个表的定义创建表：

`create table {{table_name}} like {{another_table}};`

- 向表中添加分区：

`alter table {{table_name}} add partition ({{partition_spec}});`

- 从表中删除分区：

`alter table {{table_name}} drop partition ({{partition_spec}});`

- 删除表：

`drop table {{table_name}};`