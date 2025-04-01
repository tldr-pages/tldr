# transfersh

> transfer.sh 的非官方命令行客户端。
> 更多信息： <https://github.com/AlpixTM/transfersh>.

- 上传文件到 transfer.sh:

`transfersh {{path/to/file}}`

- 上传文件时显示进度条（需要 Python 包 `requests_toolbelt`）:

`transfersh --progress {{path/to/file}}`

- 使用不同的文件名上传文件:

`transfersh --name {{filename}} {{path/to/file}}`

- 上传文件到自定义的 transfer.sh 服务器:

`transfersh --servername {{upload.server.name}} {{path/to/file}}`

- 递归上传目录中的所有文件:

`transfersh --recursive {{path/to/directory/}}`

- 以未压缩的 tar 格式上传特定目录:

`transfersh -rt {{path/to/directory}}`