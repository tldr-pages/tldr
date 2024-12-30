# starship

> 最小、极速且无限可定制的任何shell的提示。
> 一些子命令如 `init` 有自己的使用文档。
> 更多信息：<https://starship.rs>。

- 打印指定shell的starship集成代码：

`starship init {{bash|elvish|fish|ion|powershell|tcsh|zsh|nu|xonsh|cmd}}`

- 解释当前提示的每个部分，并显示渲染这些部分所花费的时间：

`starship explain`

- 打印计算出的starship配置（使用 `--default` 打印默认配置）：

`starship print-config`

- 列出支持的模块：

`starship module --list`

- 在默认编辑器中编辑starship配置：

`starship configure`

- 创建一个包含系统和starship配置相关信息的bug报告GitHub问题：

`starship bug-report`

- 打印指定shell的补全脚本：

`starship completions {{bash|elvish|fish|powershell|zsh}}`

- 显示子命令的帮助：

`starship {{subcommand}} --help`