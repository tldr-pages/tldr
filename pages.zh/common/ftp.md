# ftp

> 通过文件传输协议与服务器交互的工具。
> 更多信息：<https://manned.org/ftp>。

- 连接到FTP服务器：

`ftp {{ftp.example.com}}`

- 通过指定IP地址和端口连接到FTP服务器：

`ftp {{ip_address}} {{port}}`

- 切换到二进制传输模式（图形、压缩文件等）：

`binary`

- 在传输多个文件时不询问每个文件的确认：

`prompt off`

- 下载多个文件（通配符表达式）：

`mget {{*.png}}`

- 上传多个文件（通配符表达式）：

`mput {{*.zip}}`

- 删除远程服务器上的多个文件：

`mdelete {{*.txt}}`

- 重命名远程服务器上的文件：

`rename {{original_filename}} {{new_filename}}`