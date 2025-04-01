# mpremote

> 远程控制 MicroPython 设备。
> 更多信息：<https://docs.micropython.org/en/latest/reference/mpremote.html>.

- 列出所有连接的 MicroPython 设备：

`mpremote connect list`

- 与连接的设备打开一个交互式 REPL 会话：

`mpremote connect {{device}}`

- 在连接的设备上运行本地脚本：

`mpremote run {{path/to/script.py}}`

- 将本地目录挂载到设备：

`mpremote mount {{path/to/directory}}`

- 在设备上安装一个 mip 包：

`mpremote mip install {{package}}`
