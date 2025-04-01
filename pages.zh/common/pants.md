# pants

> 快速、可扩展、用户友好、开源的构建和开发工作流工具。
> 更多信息：<https://www.pantsbuild.org/2.20/docs/using-pants/command-line-help>.

- 列出所有目标：

`pants list ::`

- 运行所有测试：

`pants test ::`

- 修复、格式化和检查未提交的文件：

`pants --changed-since=HEAD fix fmt lint`

- 仅为未提交的文件及其依赖项进行类型检查：

`pants --changed-since=HEAD --changed-dependents=transitive check`

- 为指定的目标创建可分发的包：

`pants package {{path/to/directory:target-name}}`

- 为新的源文件自动生成 BUILD 文件目标：

`pants tailor ::`

- 显示帮助信息：

`pants help`