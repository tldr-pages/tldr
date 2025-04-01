# rbash

> 限制型 Bash shell，等同于 `bash --restricted`。
> 不允许更改工作目录、重定向命令输出或修改环境变量等。
> 有关历史展开的更多信息，请参见 `histexpand`。
> 更多信息：<https://www.gnu.org/software/bash/manual/html_node/The-Restricted-Shell>.

- 启动一个交互式 shell 会话：

`rbash`

- 执行一个命令然后退出：

`rbash -c "{{command}}"`

- 执行一个脚本：

`rbash {{path/to/script.sh}}`

- 执行一个脚本，并在执行前打印每个命令：

`rbash -x {{path/to/script.sh}}`

- 从脚本中执行命令，并在遇到第一个错误时停止：

`rbash -e {{path/to/script.sh}}`

- 从 `stdin` 读取并执行命令：

`rbash -s`
