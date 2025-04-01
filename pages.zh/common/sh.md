# sh

> Bourne shell，标准命令语言解释器。
> 有关历史扩展，请参见 `histexpand`。
> 更多信息：<https://manned.org/sh>.

- 启动一个交互式 shell 会话：

`sh`

- 执行一个命令然后退出：

`sh -c "{{command}}"`

- 执行一个脚本：

`sh {{path/to/script.sh}}`

- 从 `stdin` 读取并执行命令：

`sh -s`