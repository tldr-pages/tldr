# lftp

> 高级文件传输程序。
> 更多信息：<https://lftp.yar.ru/lftp-man.html>。

- 连接到 FTP 服务器：

`lftp --user {{username}} {{ftp.example.com}}`

- 下载多个文件（使用通配符表达式）：

`mget {{path/to/*.png}}`

- 上传多个文件（使用通配符表达式）：

`mput {{path/to/*.zip}}`

- 删除远程服务器上的多个文件：

`mrm {{path/to/*.txt}}`

- 重命名远程服务器上的文件：

`mv {{original_filename}} {{new_filename}}`

- 下载或更新整个目录：

`mirror {{path/to/remote_dir}} {{path/to/local_output_dir}}`

- 上传或更新整个目录：

`mirror -R {{path/to/local_dir}} {{path/to/remote_output_dir}}`
