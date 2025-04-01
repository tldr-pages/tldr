# http-server-upload

> 零配置命令行 HTTP 服务器，提供上传文件的轻量级接口。
> 更多信息：<https://github.com/crycode-de/http-server-upload>。

- 在默认端口启动 HTTP 服务器，将文件上传到当前目录：

`http-server-upload`

- 使用指定的最大允许文件大小（以 MiB 为单位，默认为 200 MiB）启动 HTTP 服务器：

`MAX_FILE_SIZE={{size_in_megabytes}} http-server-upload`

- 在特定端口启动 HTTP 服务器，将文件上传到当前目录：

`PORT={{port}} http-server-upload`

- 启动 HTTP 服务器，将上传的文件存储在特定目录中：

`UPLOAD_DIR={{path/to/directory}} http-server-upload`

- 使用特定目录作为上传过程中的临时文件存储位置启动 HTTP 服务器：

`UPLOAD_TMP_DIR={{path/to/directory}} http-server-upload`

- 启动接受带有特定 HTTP POST 字段令牌的上传的 HTTP 服务器：

`TOKEN={{secret}} http-server-upload`
