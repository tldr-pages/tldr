# dash

> Debian Almquist Shell，一个现代、符合 POSIX 规范的 `sh` 实现（不兼容 Bash）。
> 更多信息：<https://manned.org/dash>。

- 启动交互式 shell 会话：

`dash`

- 执行特定的 [c]ommands：

`dash -c "{{echo 'dash 已执行'}}"`

- 执行特定的脚本：

`dash {{path/to/script.sh}}`

- 检查特定脚本的语法错误：

`dash -n {{path/to/script.sh}}`

- 执行特定脚本并在执行前打印每条命令：

`dash -x {{path/to/script.sh}}`

- 执行特定脚本并在遇到第一个 [e]rror 时停止：

`dash -e {{path/to/script.sh}}`

- 从 `stdin` 执行特定的命令：

`{{echo "echo 'dash 已执行'"}} | dash`
