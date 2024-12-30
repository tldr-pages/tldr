# inotifywait

> 监视文件的更改。
> 更多信息: <https://manned.org/inotifywait>。

- 监视特定文件的事件，在第一次事件后退出：

`inotifywait {{path/to/file}}`

- 持续监视特定文件的事件而不退出：

`inotifywait --monitor {{path/to/file}}`

- 递归监视目录的事件：

`inotifywait --monitor --recursive {{path/to/directory}}`

- 监视目录的更改，排除名称与正则表达式匹配的文件：

`inotifywait --monitor --recursive --exclude "{{regular_expression}}" {{path/to/directory}}`

- 监视文件的更改，当30秒内没有事件发生时退出：

`inotifywait --monitor --timeout {{30}} {{path/to/file}}`

- 仅监视文件的修改事件：

`inotifywait --event {{modify}} {{path/to/file}}`

- 监视文件，仅打印事件，不显示状态信息：

`inotifywait --quiet {{path/to/file}}`

- 当文件被访问时运行命令：

`inotifywait --event {{access}} {{path/to/file}} && {{command}}`