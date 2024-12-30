# airshare

> 在本地网络中的两台机器之间传输数据。
> 更多信息：<https://airshare.rtfd.io/en/latest/cli.html>。

- 共享文件或目录：

`airshare {{代码}} {{路径/到/文件或目录1 路径/到/文件或目录2 ...}}`

- 接收文件：

`airshare {{代码}}`

- 主办接收服务器（使用此命令以便能够通过网页界面上传文件）：

`airshare --upload {{代码}}`

- 将文件或目录发送到接收服务器：

`airshare --upload {{代码}} {{路径/到/文件或目录1 路径/到/文件或目录2 ...}}`

- 发送已复制到剪贴板的文件路径：

`airshare --file-path {{代码}}`

- 接收文件并将其复制到剪贴板：

`airshare --clip-receive {{代码}}`