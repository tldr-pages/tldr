# gh 完成

> 为 GitHub CLI 命令生成 shell 完成脚本。
> 更多信息：<https://cli.github.com/manual/gh_completion>。

- 打印完成脚本：

`gh completion --shell {{bash|zsh|fish|powershell}}`

- 将 `gh` 完成脚本追加到 `~/.bashrc`：

`gh completion --shell {{bash}} >> {{~/.bashrc}}`

- 将 `gh` 完成脚本追加到 `~/.zshrc`：

`gh completion --shell {{zsh}} >> {{~/.zshrc}}`

- 显示子命令帮助：

`gh completion`