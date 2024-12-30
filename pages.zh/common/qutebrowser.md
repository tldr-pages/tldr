# qutebrowser

> 一款基于 PyQt5 的以键盘为驱动、类似 vim 的浏览器。
> 更多信息：<https://qutebrowser.org/>.

- 使用指定的存储目录打开 qutebrowser：

`qutebrowser --basedir {{path/to/directory}}`

- 使用临时设置打开 qutebrowser 实例：

`qutebrowser --set {{content.geolocation}} {{true|false}}`

- 恢复 qutebrowser 实例的命名会话：

`qutebrowser --restore {{session_name}}`

- 启动 qutebrowser，使用指定方法打开所有 URL：

`qutebrowser --target {{auto|tab|tab-bg|tab-silent|tab-bg-silent|window|private-window}}`

- 使用临时基础目录打开 qutebrowser，并将日志以 JSON 格式打印到 `stdout`：

`qutebrowser --temp-basedir --json-logging`