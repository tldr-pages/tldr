# dbt

> 用于在数据仓库中建模转换的工具。
> 更多信息：<https://github.com/dbt-labs/dbt-core>。

- 调试 dbt 项目和数据库连接：

`dbt debug`

- 运行项目中的所有模型：

`dbt run`

- 运行 `example_model` 的所有测试：

`dbt test --select example_model`

- 构建（加载种子、运行模型、快照和相关测试）`example_model` 及其下游依赖项：

`dbt build --select example_model+`

- 构建所有模型，但不包括标记为 `not_now` 的模型：

`dbt build --exclude "tag:not_now"`

- 构建标记为 `one` 和 `two` 的所有模型：

`dbt build --select "tag:one,tag:two"`

- 构建标记为 `one` 或 `two` 的所有模型：

`dbt build --select "tag:one tag:two"`
