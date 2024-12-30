# tftp

> 简单文件传输协议客户端。
> 更多信息：<https://manned.org/tftp.1>。

- 通过指定IP地址和端口连接到TFTP服务器：

`tftp {{server_ip}} {{port}}`

- 连接到TFTP服务器并执行TFTP [命令]：

`tftp {{server_ip}} -c {{command}}`

- 使用IPv6连接到TFTP服务器，并强制来源端口在[R]范围内：

`tftp {{server_ip}} -6 -R {{port}}:{{port}}`

- 通过tftp客户端将传输模式设置为二进制或ASCII：

`mode {{binary|ascii}}`

- 通过tftp客户端从服务器下载文件：

`get {{file}}`

- 通过tftp客户端将文件上传到服务器：

`put {{file}}`

- 退出tftp客户端：

`quit`