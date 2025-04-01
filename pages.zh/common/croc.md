# croc

> 轻松且安全地通过任何网络发送和接收文件。
> 更多信息：<https://github.com/schollz/croc>.

- 发送文件或目录：

`croc send {{path/to/file_or_directory}}`

- 使用特定的密码发送文件或目录：

`croc send --code {{passphrase}} {{path/to/file_or_directory}}`

- 在接收方机器上接收文件或目录：

`croc {{passphrase}}`

- 通过自定义中继发送并连接：

`croc --relay {{ip_to_relay}} send {{path/to/file_or_directory}}`

- 通过自定义中继接收并连接：

`croc --relay {{ip_to_relay}} {{passphrase}}`

- 在默认端口上托管一个 croc 中继：

`croc relay`

- 显示 croc 命令的参数和选项：

`croc {{send|relay}} --help`
