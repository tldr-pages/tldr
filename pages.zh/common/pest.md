# pest

> 一个注重简单性的 PHP 测试框架。
> 更多信息：<https://pestphp.com>.

- 在当前目录中初始化标准的 Pest 配置：

`pest --init`

- 运行当前目录中的测试：

`pest`

- 运行带有指定组标记的测试：

`pest --group {{name}}`

- 运行测试并打印覆盖率报告到 `stdout`：

`pest --coverage`

- 运行测试并检查覆盖率是否低于最低百分比，如果低于则失败：

`pest --coverage --min={{80}}`

- 并行运行测试：

`pest --parallel`

- 运行带有变异的测试：

`pest --mutate`
