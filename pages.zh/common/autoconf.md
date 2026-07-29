# autoconf

> 自动生成配置脚本，用于自动配置软件源码包。
> 更多信息：<https://manned.org/autoconf>。

- 从 `configure.ac`（如果存在）或 `configure.in` 生成配置脚本并保存到 `configure`：

`autoconf`

- 从指定模板生成配置脚本，输出到 `stdout`：

`autoconf {{模板文件}}`

- 从指定模板生成配置脚本（即使输入文件未更改）并写入文件：

`autoconf {{[-f|--force]}} {{[-o|--output]}} {{输出文件}} {{模板文件}}`
