# vitest

> 一个快速、现代的测试框架，专为 Vite 构建，提供无缝集成、TypeScript 支持，以及兼容 Jest 的 API，适用于单元测试、集成测试和快照测试。
> 更多信息：<https://vitest.dev/guide>。

- 运行所有可用的测试：

`vitest run`

- 从给定文件中运行测试套件：

`vitest run {{path/to/file1 path/to/file2 ...}}`

- 从当前目录和子目录中的文件中运行测试套件，路径与给定的正则表达式匹配：

`vitest run {{regular_expression1}} {{regular_expression2}}`

- 运行名称与给定正则表达式匹配的测试：

`vitest run --testNamePattern {{regular_expression}}`

- 监视文件的变化并自动重新运行相关测试：

`vitest`

- 运行带覆盖率的测试：

`vitest run --coverage`

- 运行所有测试，但在第一次测试失败后立即停止：

`vitest run --bail=1`

- 显示帮助信息：

`vitest --help`