# 自动配置

> 生成配置脚本，自动配置软件源码包。
> 更多信息：<https://www.gnu.org/software/autoconf>。

- 从 `configure.ac`（如果存在）或 `configure.in` 生成配置脚本，并将此脚本保存到 `configure`：

`autoconf`

- 从指定模板生成配置脚本；输出到 `stdout`：

`autoconf {{模板文件}}`

- 从指定模板生成配置脚本（即使输入文件未更改）并将输出写入文件：

`autoconf --force --output {{输入文件}} {{模板文件}}`
