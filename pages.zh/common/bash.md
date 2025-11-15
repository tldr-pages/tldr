# bash

> Bourne-Again SHell，兼容 `sh` 的命令行解释器。
> 此外请参阅：`zsh`，`histexpand`（历史展开）。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#Invoking-Bash>.

- 启动交互式 shell：

`bash`

- 启动一个不加载启动配置的交互式的 shell 会话：

`bash --norc`

- 执行命令：

`bash -c "{{echo '已执行bash命令'}}"`

- 执行脚本文件：

`bash {{路径/到/脚本文件.sh}}`

- 执行脚本文件，并将所有执行过的命令输出到终端：

`bash -x {{路径/到/脚本文件.sh}}`

- 执行脚本文件，并在第一个错误处终止：

`bash -e {{路径/到/脚本文件.sh}}`

- 从 `stdin` 执行指定的命令：

`{{echo "echo '已执行bash命令'"}} | bash`

- 启动一个限制的 shell 会话：

`bash -r`
