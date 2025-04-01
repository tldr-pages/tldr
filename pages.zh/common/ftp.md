# ftp

> 用于通过文件传输协议与服务器进行交互的工具。
> 更多信息：<https://manned.org/ftp>。

- 连接到 FTP 服务器：

`ftp {{ftp.example.com}}`

- 通过指定 IP 地址和端口连接到 FTP 服务器：

`ftp {{ip_address}} {{port}}`

- 切换到二进制传输模式（图形文件、压缩文件等）：

`binary`

- 传输多个文件时，不提示确认每个文件：

`prompt off`

- 下载多个文件（使用通配符表达式）：

`mget {{*.png}}`

- 上传多个文件（使用通配符表达式）：

`mput {{*.zip}}`

- 在远程服务器上删除多个文件：

`mdelete {{*.txt}}`

- 在远程服务器上重命名文件：

`rename {{original_filename}} {{new_filename}}`
