# inotifywait

> 等待文件的变化。
> 更多信息：<https://manned.org/inotifywait>.

- 监视特定文件的事件，发生第一个事件后退出：

`inotifywait {{path/to/file}}`

- 持续监视特定文件的事件，不退出：

`inotifywait --monitor {{path/to/file}}`

- 递归监视目录的事件：

`inotifywait --monitor --recursive {{path/to/directory}}`

- 监视目录的变化，排除名称匹配正则表达式的文件：

`inotifywait --monitor --recursive --exclude "{{regular_expression}}" {{path/to/directory}}`

- 监视文件的变化，30秒内没有事件发生时退出：

`inotifywait --monitor --timeout {{30}} {{path/to/file}}`

- 只监视文件的修改事件：

`inotifywait --event {{modify}} {{path/to/file}}`

- 监视文件，只打印事件，不打印状态消息：

`inotifywait --quiet {{path/to/file}}`

- 当文件被访问时运行命令：

`inotifywait --event {{access}} {{path/to/file}} && {{command}}`