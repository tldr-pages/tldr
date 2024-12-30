# pkgin

> 在 NetBSD 上管理 `pkgsrc` 二进制包。
> 更多信息：<https://pkgin.net/#usage>。

- 安装一个包：

`pkgin install {{package}}`

- 移除一个包及其依赖：

`pkgin remove {{package}}`

- 升级所有包：

`pkgin full-upgrade`

- 搜索一个包：

`pkgin search {{keyword}}`

- 列出已安装的包：

`pkgin list`

- 移除不需要的依赖：

`pkgin autoremove`