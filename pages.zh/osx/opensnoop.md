# opensnoop

> 跟踪您系统上的文件打开情况。
> 更多信息：<https://keith.github.io/xcode-man-pages/opensnoop.1m.html>。

- 打印所有文件打开事件：

`sudo opensnoop`

- 按名称跟踪某个进程打开的所有文件：

`sudo opensnoop -n "{{process_name}}"`

- 按PID跟踪某个进程打开的所有文件：

`sudo opensnoop -p {{PID}}`

- 跟踪哪些进程打开了指定的文件：

`sudo opensnoop -f {{path/to/file}}`