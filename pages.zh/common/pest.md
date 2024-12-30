# Pest

> 一个专注于简单性的 PHP 测试框架。
> 更多信息：<https://pestphp.com>。

- 在当前目录中初始化标准 Pest 配置：

`pest --init`

- 在当前目录中运行测试：

`pest`

- 运行带有指定组注释的测试：

`pest --group {{name}}`

- 运行测试并将覆盖率报告打印到 `stdout`：

`pest --coverage`

- 运行测试并在覆盖率低于最低百分比时失败：

`pest --coverage --min={{80}}`

- 并行运行测试：

`pest --parallel`

- 运行带有变异的测试：

`pest --mutate`