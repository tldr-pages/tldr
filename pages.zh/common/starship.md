# starship

> 适用于任何 Shell 的最小、超快速且无限可定制的命令提示符。
> 某些子命令（如 `init`）有自己的使用文档。
> 更多信息：<https://starship.rs>。

- 打印为指定 Shell 生成的 Starship 集成代码：

`starship init {{bash|elvish|fish|ion|powershell|tcsh|zsh|nu|xonsh|cmd}}`

- 解释当前提示符的每一部分并显示渲染它们所花费的时间：

`starship explain`

- 打印计算出的 Starship 配置（使用 `--default` 打印默认配置）：

`starship print-config`

- 列出支持的模块：

`starship module --list`

- 在默认编辑器中编辑 Starship 配置：

`starship configure`

- 创建一个预填充了系统信息和 Starship 配置的 GitHub Bug 报告：

`starship bug-report`

- 打印为指定 Shell 生成的补全脚本：

`starship completions {{bash|elvish|fish|powershell|zsh}}`

- 显示子命令的帮助信息：

`starship {{subcommand}} --help`