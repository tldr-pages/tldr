# circup

> CircuitPython 库更新器。
> 更多信息：<https://github.com/adafruit/circup>。

- 以交互方式更新设备上的模块：

`circup update`

- 安装一个新库：

`circup install {{library_name}}`

- 搜索一个库：

`circup show {{partial_name}}`

- 列出连接设备上所有库的 `requirements.txt` 格式：

`circup freeze`

- 将连接设备上所有库保存在当前目录：

`circup freeze -r`