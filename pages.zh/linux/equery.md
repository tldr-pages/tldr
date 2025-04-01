# equery

> 查看 Portage 软件包的信息。
> 更多信息：<https://wiki.gentoo.org/wiki/Equery>。

- 列出所有已安装的软件包：

`equery list '*'`

- 在 Portage 树和叠加层中搜索已安装的软件包：

`equery list -po {{package1 package2 ...}}`

- 列出所有依赖于给定软件包的软件包：

`equery depends {{package}}`

- 列出给定软件包依赖的所有软件包：

`equery depgraph {{package}}`

- 列出由软件包安装的所有文件：

`equery files --tree {{package}}`