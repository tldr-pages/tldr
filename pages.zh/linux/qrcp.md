# qrcp

> 文件传输工具。
> 更多信息：<https://github.com/claudiodangelis/qrcp>.

- 发送文件或目录：

`qrcp send {{path/to/file_or_directory path/to/file_directory ...}}`

- 接收文件：

`qrcp receive`

- 在传输前压缩内容：

`qrcp send --zip {{path/to/file_or_directory}}`

- 使用指定的端口：

`qrcp {{send|receive}} {{[-p|--port]}} {{port_number}}`

- 使用指定的网络接口：

`qrcp {{send|receive}} {{[-i|--interface]}} {{interface}}`

- 保持服务器运行：

`qrcp {{send|receive}} --keep-alive`