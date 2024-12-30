# 感染

> 一个用于 PHP 的突变测试框架。
> 更多信息：<https://infection.github.io>。

- 使用配置文件分析代码（如果不存在则创建一个）：

`infection`

- 使用特定数量的线程：

`infection --threads {{线程数}}`

- 指定最低突变评分指标（MSI）：

`infection --min-msi {{百分比}}`

- 指定最低覆盖代码 MSI：

`infection --min-covered-msi {{百分比}}`

- 使用特定的测试框架（默认为 PHPUnit）：

`infection --test-framework {{phpunit|phpspec}}`

- 仅突变被测试覆盖的代码行：

`infection --only-covered`

- 显示已应用的突变代码：

`infection --show-mutations`

- 指定日志详细程度：

`infection --log-verbosity {{default|all|none}}`