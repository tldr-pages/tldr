# lftp

> 高级文件传输程序。
> 更多信息：<https://lftp.yar.ru/lftp-man.html>。

- 连接到FTP服务器：

`lftp --user {{用户名}} {{ftp.example.com}}`

- 下载多个文件（通配符表达式）：

`mget {{path/to/*.png}}`

- 上传多个文件（通配符表达式）：

`mput {{path/to/*.zip}}`

- 在远程服务器上删除多个文件：

`mrm {{path/to/*.txt}}`

- 在远程服务器上重命名文件：

`mv {{原文件名}} {{新文件名}}`

- 下载或更新整个目录：

`mirror {{path/to/remote_dir}} {{path/to/local_output_dir}}`

- 上传或更新整个目录：

`mirror -R {{path/to/local_dir}} {{path/to/remote_output_dir}}`