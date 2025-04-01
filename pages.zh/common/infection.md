# infection

> 一个 PHP 的变异测试框架。
> 更多信息：<https://infection.github.io>.

- 使用配置文件（或创建一个配置文件，如果它不存在）分析代码：

`infection`

- 使用指定数量的线程：

`infection --threads {{线程数}}`

- 指定最低的变异评分指标（MSI）：

`infection --min-msi {{百分比}}`

- 指定最低的已覆盖代码的 MSI：

`infection --min-covered-msi {{百分比}}`

- 使用特定的测试框架（默认为 PHPUnit）：

`infection --test-framework {{phpunit|phpspec}}`

- 仅变异被测试覆盖的代码行：

`infection --only-covered`

- 显示已应用的变异代码：

`infection --show-mutations`

- 指定日志详细程度：

`infection --log-verbosity {{default|all|none}}`