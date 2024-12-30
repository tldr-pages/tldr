# dash

> Debian Almquist Shell，是一个现代的、符合POSIX标准的 `sh` 实现（不兼容Bash）。
> 更多信息：<https://manned.org/dash>。

- 启动一个交互式shell会话：

`dash`

- 执行特定的 [c]ommands：

`dash -c "{{echo 'dash is executed'}}"`

- 执行特定脚本：

`dash {{path/to/script.sh}}`

- 检查特定脚本的语法错误：

`dash -n {{path/to/script.sh}}`

- 执行特定脚本，同时在执行每个命令之前打印该命令：

`dash -x {{path/to/script.sh}}`

- 执行特定脚本，并在遇到第一个 [e]rror 时停止：

`dash -e {{path/to/script.sh}}`

- 从 `stdin` 执行特定命令：

`{{echo "echo 'dash is executed'"}} | dash`