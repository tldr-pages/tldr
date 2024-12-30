# aria2c

> 快速下载工具。
> 支持 HTTP(S)、FTP、SFTP、BitTorrent 和 Metalink。
> 更多信息：<https://aria2.github.io>。

- 下载特定的 URI 到文件：

`aria2c "{{url}}"`

- 从 URI 下载文件并指定输出名称：

`aria2c --out {{path/to/file}} "{{url}}"`

- 并行下载多个不同的文件：

`aria2c --force-sequential {{false}} "{{url1 url2 ...}}"`

- 从不同的镜像下载相同的文件并验证下载文件的校验和：

`aria2c --checksum {{sha-256}}={{hash}} "{{url1}}" "{{url2}}" "{{urlN}}"`

- 下载文件中列出的 URI，并指定并行下载的数量：

`aria2c --input-file {{path/to/file}} --max-concurrent-downloads {{number_of_downloads}}`

- 使用多个连接下载：

`aria2c --split {{number_of_connections}} "{{url}}"`

- 使用用户名和密码进行 FTP 下载：

`aria2c --ftp-user {{username}} --ftp-passwd {{password}} "{{url}}"`

- 限制下载速度（字节/秒）：

`aria2c --max-download-limit {{speed}} "{{url}}"`