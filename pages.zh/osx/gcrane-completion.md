# gcrane 自动完成

> 为指定的 shell 生成 gcrane 的自动完成脚本。
> 可用的 shell 包括 `bash`、`fish`、`powershell` 和 `zsh`。
> 更多信息：<https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>。

- 为您的 shell 生成自动完成脚本：

`gcrane completion {{shell_name}}`

- 禁用完成描述：

`gcrane completion {{shell_name}} --no-descriptions`

- 在当前 shell 会话中加载完成（bash/zsh）：

`source <(gcrane completion bash/zsh)>`

- 在当前 shell 会话中加载完成（fish）：

`gcrane completion fish | source`

- 为每个新会话加载完成（bash）：

`gcrane completion bash > $(brew --prefix)/etc/bash_completion.d/gcrane`

- 为每个新会话加载完成（zsh）：

`gcrane completion zsh > $(brew --prefix)/share/zsh/site-functions/_gcrane`

- 为每个新会话加载完成（fish）：

`gcrane completion fish > ~/.config/fish/completions/gcrane.fish`

- 显示帮助：

`gcrane completion {{shell_name}} {{-h|--help}}`