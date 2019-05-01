# aria2c

> 快速下载工具.
> 支持 HTTP(S), FTP, SFTP, BitTorrent, and Metalink.

- 下载一个URI到文件:

`aria2c {{url}}`

- 从多个源处下载一个资源:

`aria2c {{url_1}} {{url_2}}`

- 通过保存在一个文件中的URL列表来下载资源:

`aria2c -i {{文件名}}`

- 使用多个连接下载资源:

`aria2c -s {{连接数量}} {{url}}`

- 通过带用户名密码验证的FTP协议下载资源:

`aria2c --ftp-user={{用户名}} --ftp-passwd={{密码}} {{url}}`

- 限制下载速度 (bytes/s):

`aria2c --max-download-limit={{速度}} {{url}}`
