# kahlan

> 一个用于 PHP 的单元测试和行为驱动开发测试框架。
> 更多信息：<https://kahlan.github.io>。

- 运行 "spec" 目录下的所有测试规范：

`kahlan`

- 使用特定的配置文件运行测试规范：

`kahlan --config={{path/to/configuration_file}}`

- 使用 reporter 输出运行测试规范的结果：

`kahlan --reporter={{dot|bar|json|tap|verbose}}`

- 运行测试规范并生成代码覆盖率报告（详细级别可在 0 到 4 之间选择）：

`kahlan --coverage={{detail_level}}`