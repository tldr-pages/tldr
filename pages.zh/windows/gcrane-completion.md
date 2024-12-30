# gcrane 自动补全

> 为指定的 shell 生成 gcrane 的自动补全脚本。
> 可用的 shell 包括 `bash`、`fish`、`powershell` 和 `zsh`。
> 更多信息请查看: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>。

- 为您的 shell 生成自动补全脚本：

`gcrane completion {{shell_name}}`

- 禁用补全描述：

`gcrane completion {{shell_name}} --no-descriptions`

- 在当前 shell 会话中加载补全（powershell）：

`gcrane completion powershell | Out-String | Invoke-Expression`

- 为每个新会话加载补全（powershell）：

`gcrane completion powershell | Out-String | Invoke-Expression`

- 显示帮助信息：

`gcrane completion {{shell_name}} {{-h|--help}}`