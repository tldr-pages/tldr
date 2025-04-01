# miniserve

> 简单的 HTTP 文件服务器。
> 更多信息：<https://github.com/svenstaro/miniserve>。

- 服务一个目录：

`miniserve {{path/to/directory}}`

- 服务单个文件：

`miniserve {{path/to/file}}`

- 使用 HTTP 基本认证服务一个目录：

`miniserve --auth {{username}}:{{password}} {{path/to/directory}}`