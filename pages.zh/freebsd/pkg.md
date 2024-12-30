# pkg

> FreeBSD 包管理器。
> 更多信息：<https://man.freebsd.org/cgi/man.cgi?pkg>。

- 安装新包：

`pkg install {{package}}`

- 删除一个包：

`pkg delete {{package}}`

- 升级所有包：

`pkg upgrade`

- 搜索一个包：

`pkg search {{keyword}}`

- 列出已安装的包：

`pkg info`

- 移除不需要的依赖：

`pkg autoremove`