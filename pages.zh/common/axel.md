# axel

> 一款下载加速器。
> 支持 HTTP、HTTPS 和 FTP.
> 更多信息：<https://github.com/axel-download-accelerator/axel>.

- 链接下载：

`axel {{超链接}}`

- 链接下载，指定文件名：

`axel {{超链接}} -o {{文件名称}}`

- 多连接数下载：

`axel -n {{连接数量}} {{超链接}}`

- 查询镜像：

`axel -S {{镜像数量}} {{超链接}}`

- 限制下载速度（字节 bite 每秒）：

`axel -s {{字节数}} {{超链接}}`
