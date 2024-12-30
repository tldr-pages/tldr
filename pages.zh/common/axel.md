# axel

> 下载加速器。
> 支持 HTTP、HTTPS 和 FTP。
> 更多信息：<https://github.com/axel-download-accelerator/axel>。

- 下载一个 URL 到文件：

`axel {{url}}`

- 下载并指定一个 [o]utput 文件：

`axel {{url}} -o {{path/to/file}}`

- 使用特定的 [n] 连接数下载：

`axel -n {{connections_num}} {{url}}`

- [S]earch for mirrors:

`axel -S {{mirrors_num}} {{url}}`

- 限制下载 [s]peed（每秒字节数）：

`axel -s {{speed}} {{url}}`