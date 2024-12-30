# bash

> Bourne-Again SHell，一个与 `sh` 兼容的命令行解释器。
> 另见：`zsh`，`histexpand`（历史扩展）。
> 更多信息：<https://www.gnu.org/software/bash/>。

- 启动一个交互式 shell 会话：

`bash`

- 启动一个不加载启动配置的交互式 shell 会话：

`bash --norc`

- 执行特定的 [c]ommands：

`bash -c "{{echo 'bash is executed'}}"`

- 执行特定脚本：

`bash {{path/to/script.sh}}`

- E[x]ecute 特定脚本，在执行每个命令之前打印该命令：

`bash -x {{path/to/script.sh}}`

- 执行特定脚本并在第一个 [e]rror 处停止：

`bash -e {{path/to/script.sh}}`

- 从 `stdin` 执行特定命令：

`{{echo "echo 'bash is executed'"}} | bash`

- 启动一个 [r]estricted shell 会话：

`bash -r`