# bind

> Bash 内置命令，用于管理 bash 热键和变量。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-bind>.

- 列出所有已绑定的命令及其热键：

`bind {{-p|-P}}`

- 查询命令的热键：

`bind -q {{command}}`

- 绑定一个键：

`bind -x '"{{key_sequence}}":{{command}}'`

- 列出用户定义的绑定：

`bind -X`

- 显示帮助：

`help bind`
