# golangci-lint

> 并行化、智能且快速的Go代码检查器运行器，支持所有主要的IDE并支持YAML配置。
> 更多信息请访问：<https://golangci-lint.run/welcome/quick-start/>.

- 在当前文件夹中运行代码检查器：

`golangci-lint run`

- 列出已启用和已禁用的检查器（注意：已禁用的检查器显示在最后，请不要将它们误认为已启用的检查器）：

`golangci-lint linters`

- [E]nable为此运行启用特定的检查器：

`golangci-lint run --enable {{linter}}`