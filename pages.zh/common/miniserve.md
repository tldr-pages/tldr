# miniserve

> 简单的 HTTP 文件服务器。
> 更多信息：<https://github.com/svenstaro/miniserve>。

- 提供一个目录：

`miniserve {{路径/到/目录}}`

- 提供一个单独的文件：

`miniserve {{路径/到/文件}}`

- 使用 HTTP 基本认证提供一个目录：

`miniserve --auth {{用户名}}:{{密码}} {{路径/到/目录}}`