# axel

> 一款下载加速器。
> 支持 HTTP、HTTPS 和 FTP。
> 另请参阅：`aria2c`。
> 更多信息：<https://manned.org/axel>。

- 链接下载：

`axel {{超链接}}`

- 链接下载，指定文件名：

`axel {{超链接}} {{[-o|--output]}} {{路径/到/文件}}`

- 多连接数下载：

`axel {{[-n|--num-connections]}} {{连接数量}} {{超链接}}`

- 查询镜像：

`axel {{[-S|--search=]}}{{镜像数量}} {{超链接}}`

- 限制下载速度（字节 bite 每秒）：

`axel {{[-s|--max-speed]}} {{字节数}} {{超链接}}`
