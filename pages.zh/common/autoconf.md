# autoconf

> 生成用于自动配置软件源代码包的配置脚本。
> 更多信息：<https://manned.org/autoconf>.

- 从 `configure.ac`（如果存在）或 `configure.in` 生成一个配置脚本，并将该脚本保存为 `configure`：

`autoconf`

- 从指定的模板生成一个配置脚本；输出到 `stdout`（标准输出）：

`autoconf {{模板文件}}`

- 从指定的模板生成一个配置脚本（即使输入文件没有发生变化），并将输出写入到一个文件中：

`autoconf {{[-f|--force]}} {{[-o|--output]}} {{输出文件}} {{模板文件}}`
