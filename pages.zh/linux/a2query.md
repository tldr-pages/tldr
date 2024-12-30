# a2query

> 从基于Debian的操作系统中检索Apache的运行时配置。
> 更多信息：<https://manned.org/a2query>。

- 列出已启用的Apache模块：

`sudo a2query -m`

- 检查特定模块是否已安装：

`sudo a2query -m {{module_name}}`

- 列出已启用的虚拟主机：

`sudo a2query -s`

- 显示当前启用的多处理模块：

`sudo a2query -M`

- 显示Apache版本：

`sudo a2query -v`