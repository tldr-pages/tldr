# cadaver

> 用于 Unix 的 WebDAV 客户端。
> 更多信息：<https://manned.org/cadaver>.

- 连接到服务器 <dav.example.com>，打开根集合：

`cadaver {{http://dav.example.com/}}`

- 使用特定端口连接到服务器，并打开集合 `/foo/bar/`：

`cadaver {{http://dav.example.com:8022/foo/bar/}}`

- 使用 SSL 连接到服务器：

`cadaver {{https://davs.example.com/}}`