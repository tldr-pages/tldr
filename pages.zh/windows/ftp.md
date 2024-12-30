# ftp

> 交互式地在本地和远程 FTP 服务器之间传输文件。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/ftp>。

- 交互式连接到远程 FTP 服务器：

`ftp {{host}}`

- 以匿名用户身份登录：

`ftp -A {{host}}`

- 禁用初始连接时的自动登录：

`ftp -n {{host}}`

- 运行包含 FTP 命令列表的文件：

`ftp -s:{{path\to\file}} {{host}}`

- 下载多个文件（通配符表达式）：

`mget {{*.png}}`

- 上传多个文件（通配符表达式）：

`mput {{*.zip}}`

- 删除远程服务器上的多个文件：

`mdelete {{*.txt}}`

- 显示帮助信息：

`ftp --help`