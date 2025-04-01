# cradle install

> 安装 Cradle PHP 框架组件。
> 更多信息：<https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#install>.

- 安装 Cradle 的组件（用户将被提示输入更多详细信息）：

`cradle install`

- 强制覆盖文件：

`cradle install --force`

- 跳过运行 SQL 迁移：

`cradle install --skip-sql`

- 跳过运行包更新：

`cradle install --skip-versioning`

- 使用特定的数据库详细信息：

`cradle install -h {{hostname}} -u {{username}} -p {{password}}`
