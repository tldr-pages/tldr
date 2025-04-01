# xrdb

> X 窗口服务器的资源数据库工具，适用于类 Unix 系统。
> 更多信息：<https://www.x.org/releases/X11R7.7/doc/man/man1/xrdb.1.xhtml>.

- 以交互模式启动 `xrdb`：

`xrdb`

- 从资源文件加载值（例如样式规则）：

`xrdb -load {{~/.Xresources}}`

- 查询资源数据库并打印当前设置的值：

`xrdb -query`
