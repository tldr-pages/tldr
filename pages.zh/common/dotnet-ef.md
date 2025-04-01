# dotnet ef

> 执行 Entity Framework Core 的设计时开发任务。
> 更多信息：<https://learn.microsoft.com/ef/core/cli/dotnet>.

- 更新数据库到指定的迁移：

`dotnet ef database update {{migration}}`

- 删除数据库：

`dotnet ef database drop`

- 列出可用的 `DbContext` 类型：

`dotnet ef dbcontext list`

- 为数据库生成 `DbContext` 和实体类型的代码：

`dotnet ef dbcontext scaffold {{connection_string}} {{provider}}`

- 添加新的迁移：

`dotnet ef migrations add {{name}}`

- 移除最后一个迁移，并回滚为该迁移所做的代码更改：

`dotnet ef migrations remove`

- 列出可用的迁移：

`dotnet ef migrations list`

- 从迁移范围生成 SQL 脚本：

`dotnet ef migrations script {{from_migration}} {{to_migration}}`