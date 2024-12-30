# Pants

> 快速、可扩展、用户友好的开源构建和开发工作流程工具。
> 更多信息：<https://www.pantsbuild.org/2.20/docs/using-pants/command-line-help>。

- 列出所有目标：

`pants list ::`

- 运行所有测试：

`pants test ::`

- 仅修复、格式化和检查未提交的文件：

`pants --changed-since=HEAD fix fmt lint`

- 仅对未提交的文件及其依赖项进行类型检查：

`pants --changed-since=HEAD --changed-dependents=transitive check`

- 为指定目标创建可分发包：

`pants package {{path/to/directory:target-name}}`

- 为新源文件自动生成 BUILD 文件目标：

`pants tailor ::`

- 显示帮助：

`pants help`