# autoconf

> 生成配置脚本以自动配置软件源代码包。
> 更多信息：<https://www.gnu.org/software/autoconf>。

- 从 `configure.ac`（如果存在）或 `configure.in` 生成配置脚本，并将此脚本保存为 `configure`：

`autoconf`

- 从指定模板生成配置脚本；输出到 `stdout`：

`autoconf {{template-file}}`

- 从指定模板生成配置脚本（即使输入文件没有改变）并将输出写入文件：

`autoconf --force --output {{outfile}} {{template-file}}`