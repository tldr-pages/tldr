# http-server-upload

> 零配置的命令行HTTP服务器，提供轻量级接口用于上传文件。
> 更多信息：<https://github.com/crycode-de/http-server-upload>。

- 在默认端口启动HTTP服务器，以便将文件上传到当前目录：

`http-server-upload`

- 启动HTTP服务器，并指定允许的最大上传文件大小（默认为200 MiB）：

`MAX_FILE_SIZE={{size_in_megabytes}} http-server-upload`

- 在特定端口启动HTTP服务器，以便将文件上传到当前目录：

`PORT={{port}} http-server-upload`

- 启动HTTP服务器，将上传的文件存储在特定目录中：

`UPLOAD_DIR={{path/to/directory}} http-server-upload`

- 启动HTTP服务器，使用特定目录临时存储上传过程中的文件：

`UPLOAD_TMP_DIR={{path/to/directory}} http-server-upload`

- 启动HTTP服务器，接受在HTTP POST中带有特定令牌字段的上传：

`TOKEN={{secret}} http-server-upload`