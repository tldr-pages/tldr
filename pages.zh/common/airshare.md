# airshare

> 在本地网络中传输数据的工具。
> 更多信息： <https://airshare.rtfd.io/en/latest/cli.html>。

- 共享文件或目录：

`airshare {{code}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 接收文件：

`airshare {{code}}`

- 主机接收服务器（使用此选项可以通过 Web 接口上传文件）：

`airshare --upload {{code}}`

- 将文件或目录发送到接收服务器：

`airshare --upload {{code}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 发送已复制到剪贴板的文件路径：

`airshare --file-path {{code}}`

- 接收文件并将其复制到剪贴板：

`airshare --clip-receive {{code}}`
