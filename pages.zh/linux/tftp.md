# tftp

> 简单文件传输协议客户端。
> 更多信息：<https://manned.org/tftp.1>.

- 连接到指定 IP 地址和端口的 TFTP 服务器：

`tftp {{server_ip}} {{port}}`

- 连接到 TFTP 服务器并执行 TFTP [c]ommand 命令：

`tftp {{server_ip}} -c {{command}}`

- 使用 IPv6 连接到 TFTP 服务器，并强制源端口在 [R]ange 范围内：

`tftp {{server_ip}} -6 -R {{port}}:{{port}}`

- 通过 tftp 客户端设置传输模式为二进制或 ASCII：

`mode {{binary|ascii}}`

- 通过 tftp 客户端从服务器下载文件：

`get {{file}}`

- 通过 tftp 客户端将文件上传到服务器：

`put {{file}}`

- 退出 tftp 客户端：

`quit`