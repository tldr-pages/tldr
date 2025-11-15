# zsh

> Z SHell，一个兼容 Bash 的命令行解释器。
> 参见：`bash`，`histexpand`.
> 更多信息：<https://zsh.sourceforge.io/Doc/Release/Invocation.html#Invocation>.

- 启动交互式解释器：

`zsh`

- 执行指定的命令：

`zsh -c "{{echo Hello world}}"`

- 执行指定的脚本：

`zsh {{路径/到/脚本.zsh}}`

- 不执行指定的脚本，只检查其语法错误：

`zsh --no-exec {{路径/到/脚本.zsh}}`

- 执行来自 `stdin` 的命令：

`{{echo Hello world}} | zsh`

- 执行指定的脚本，并打印出每一个将要执行的命令：

`zsh --xtrace {{路径/到/脚本.zsh}}`

- 启动详细模式的交互式解释器，会打印出每一个将要执行的命令：

`zsh --verbose`

- 在 `zsh` 里执行指定的命令，但禁用 glob 模式：

`noglob {{命令}}`
