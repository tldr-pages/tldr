# gacutil

> 全局程序集缓存 (GAC) 管理工具。
> 更多信息：<https://manned.org/gacutil>.

- 将指定的程序集安装到 GAC：

`gacutil -i {{path/to/assembly.dll}}`

- 从 GAC 中卸载指定的程序集：

`gacutil -u {{assembly_display_name}}`

- 打印 GAC 的内容：

`gacutil -l`