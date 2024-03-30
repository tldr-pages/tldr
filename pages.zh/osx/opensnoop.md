# opensnoop

> 跟踪系统中打开的文件标识符。
> 更多信息：<https://keith.github.io/xcode-man-pages/opensnoop.1m.html>.

- 输出当前系统内被打开的所有文件：

`sudo opensnoop`

- 跟踪给定进程名，打开的所有文件：

`sudo opensnoop -n "{{进程名}}"`

- 跟踪给定 PID（进程号），打开的所有文件：

`sudo opensnoop -p {{PID 进程号}}`

- 跟踪打开了指定文件的继承：

`sudo opensnoop -f {{路径 / 文件}}`
