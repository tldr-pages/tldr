# aria2c

> 快速下载工具。
> 支持 HTTP(S)、FTP、SFTP、BitTorrent 和 Metalink。
> 更多信息：<https://aria2.github.io/manual/en/html/aria2c.html>.

- 将特定 URI 下载到一个文件：

`aria2c "{{url}}"`

- 从一个 URI 下载文件，并指定输出文件名：

`aria2c --out {{路径/到/文件}} "{{url}}"`

- 并行下载多个不同的文件：

`aria2c --force-sequential {{false}} "{{url1 url2 ...}}"`

- 从不同的镜像下载相同的文件，并验证已下载文件的校验和：

`aria2c --checksum {{sha-256}}={{hash}} "{{url1}}" "{{url2}}" "{{urlN}}"`

- 下载文件中列出的 URI，并指定并行下载的数量：

`aria2c --input-file {{路径/到/文件}} --max-concurrent-downloads {{下载数}}`

- 使用多个连接进行下载：

`aria2c --split {{连接数}} "{{url}}"`

- 使用用户名和密码进行 FTP 下载：

`aria2c --ftp-user {{用户名}} --ftp-passwd {{密码}} "{{url}}"`

- 限制下载速度为字节/秒（bytes/s）：

`aria2c --max-download-limit {{速度}} "{{url}}"`
