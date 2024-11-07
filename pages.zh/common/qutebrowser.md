# qutebrowser

> 一个基于 PyQt5 的类似 vim 的键盘驱动浏览器。
> 更多信息：<https://qutebrowser.org/>.

- 使用指定的存储目录打开 qutebrowser：

`qutebrowser --basedir {{路径/到/目录}}`

- 使用临时设置打开 qutebrowser 实例：

`qutebrowser --set {{content.geolocation}} {{true|false}}`

- 恢复 qutebrowser 实例的命名会话：

`qutebrowser --restore {{session_name}}`

- 启动 qutebrowser，使用指定的方法打开所有 URL：

`qutebrowser --target {{auto|tab|tab-bg|tab-silent|tab-bg-silent|window|private-window}}`

- 使用临时基础目录打开 qutebrowser 并以 JSON 形式将日志打印到 `stdout`：

`qutebrowser --temp-basedir --json-logging`
