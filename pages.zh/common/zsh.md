# zsh

> Z SHell，一个与 Bash 兼容的命令行解释器。
> 另见：`bash`，`histexpand`。
> 更多信息：<https://www.zsh.org>。

- 启动一个交互式 shell 会话：

`zsh`

- 执行特定的 [c]ommands：

`zsh -c "{{echo Hello world}}"`

- 执行特定脚本：

`zsh {{path/to/script.zsh}}`

- 检查特定脚本的语法错误而不执行它：

`zsh --no-exec {{path/to/script.zsh}}`

- 从 `stdin` 执行特定命令：

`{{echo Hello world}} | zsh`

- 执行特定脚本，在执行每个命令之前打印该命令：

`zsh --xtrace {{path/to/script.zsh}}`

- 启动一个交互式 shell 会话，处于详细模式，在执行每个命令之前打印该命令：

`zsh --verbose`

- 在 `zsh` 中执行特定命令并禁用全局模式：

`noglob {{command}}`