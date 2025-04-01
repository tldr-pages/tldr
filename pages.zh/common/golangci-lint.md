# golangci-lint

> 并行、智能且快速的 Go 代码检查工具，支持所有主要 IDE，并支持 YAML 配置。
> 更多信息：<https://golangci-lint.run/welcome/quick-start/>。

- 在当前文件夹中运行代码检查：

`golangci-lint run`

- 列出启用和禁用的代码检查器（注意：禁用的检查器显示在最后，请勿将它们误认为是启用的检查器）：

`golangci-lint linters`

- 为本次运行启用特定的代码检查器：

`golangci-lint run {{[-E|--enable]}} {{linter}}`
