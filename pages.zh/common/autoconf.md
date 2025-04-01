# autoconf

> 生成配置脚本，以自动配置软件源代码包。
> 更多信息：<https://manned.org/autoconf>.

- 从 `configure.ac`（如果存在）或 `configure.in` 生成配置脚本，并将此脚本保存为 `configure`：

`autoconf`

- 从指定的模板生成配置脚本；输出到 `stdout`：

`autoconf {{template-file}}`

- 即使输入文件未更改，也从指定的模板生成配置脚本，并将输出写入文件：

`autoconf {{[-f|--force]}} {{[-o|--output]}} {{outfile}} {{template-file}}`