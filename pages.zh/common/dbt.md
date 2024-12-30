# dbt

> 一个用于在数据仓库中建模转换的工具。
> 更多信息：<https://github.com/dbt-labs/dbt-core>。

- 调试 dbt 项目和与数据库的连接：

`dbt debug`

- 运行项目的所有模型：

`dbt run`

- 运行 `example_model` 的所有测试：

`dbt test --select example_model`

- 构建（加载种子数据，运行模型，快照和与之相关的测试）`example_model` 及其下游依赖项：

`dbt build --select example_model+`

- 构建所有模型，排除带有标签 `not_now` 的模型：

`dbt build --exclude "tag:not_now"`

- 构建所有带有标签 `one` 和 `two` 的模型：

`dbt build --select "tag:one,tag:two"`

- 构建所有带有标签 `one` 或 `two` 的模型：

`dbt build --select "tag:one tag:two"`