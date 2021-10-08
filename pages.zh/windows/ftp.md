# ftp

> 在本地和远程 FTP 服务器之间交互式传输文件。
> 更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/ftp>.

- 交互式连接一个远程的 FTP 服务：

`ftp {{主机名}}`

- 匿名登录：

`ftp -A {{主机名}}`

- 初始连接时禁用自动登录：

`ftp -n {{主机名}}`

- 运行包含 FTP 命令列表的文件：

`ftp -s:{{文件的路径}} {{主机名}}`

- 下载多个文件（通配符表达式）：

`mget {{*.png}}`

- 上传多个文件（通配符表达式）：

`mput {{*.zip}}`

- 在远程服务器上删除多个文件：

`mdelete {{*.txt}}`

- 显示详细的帮助：

`ftp --help`
