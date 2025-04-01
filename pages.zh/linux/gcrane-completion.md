# gcrane completion

> 为指定的 shell 生成 gcrane 的自动补全脚本。
> 可用的 shell 有 `bash`、`fish`、`powershell` 和 `zsh`。
> 更多信息：<https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>。

- 为你的 shell 生成自动补全脚本：

`gcrane completion {{shell_name}}`

- 禁用补全描述：

`gcrane completion {{shell_name}} --no-descriptions`

- 在当前 shell 会话中加载补全（bash/zsh）：

`source <(gcrane completion bash/zsh)`

- 在当前 shell 会话中加载补全（fish）：

`gcrane completion fish | source`

- 在每个新会话中加载补全（bash）：

`gcrane completion bash > /etc/bash_completion.d/gcrane`

- 在每个新会话中加载补全（zsh）：

`gcrane completion zsh > "${fpath[1]}/_gcrane"`

- 在每个新会话中加载补全（fish）：

`gcrane completion fish > ~/.config/fish/completions/gcrane.fish`

- 显示帮助：

`gcrane completion {{shell_name}} {{[-h|--help]}}`
