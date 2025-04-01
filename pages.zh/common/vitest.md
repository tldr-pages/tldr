# vitest

> 专为 Vite 构建的快速、现代的测试框架，提供无缝集成、TypeScript 支持和与 Jest 兼容的 API，用于单元测试、集成测试和快照测试。
> 更多信息：<https://vitest.dev/guide>.

- 运行所有可用的测试：

`vitest run`

- 运行指定文件中的测试套件：

`vitest run {{path/to/file1 path/to/file2 ...}}`

- 运行当前目录及其子目录中路径与给定正则表达式匹配的文件中的测试套件：

`vitest run {{regular_expression1}} {{regular_expression2}}`

- 运行名称与给定正则表达式匹配的测试：

`vitest run --testNamePattern {{regular_expression}}`

- 监视文件变化并自动重新运行相关测试：

`vitest`

- 带覆盖率运行测试：

`vitest run --coverage`

- 运行所有测试，但在首次测试失败后立即停止：

`vitest run --bail=1`

- 显示帮助：

`vitest --help`
