# automake

> 使用 GNU 标准为软件项目自动生成 Makefile。
> 更多信息：<https://www.gnu.org/software/automake/manual/automake.html#automake-Invocation>.

- 在编辑 `Makefile.am` 之后运行 automake 以重新生成 Makefile：

`automake`

- 为非 GNU 项目生成 `Makefile.in`（foreign 模式）：

`automake --foreign`

- 添加详细输出以便调试：

`automake {{[-v|--verbose]}}`

- 添加缺失的标准文件（INSTALL、COPYING、depcomp 等）：

`automake {{[-a|--add-missing]}}`

- 显示帮助：

`automake --help`
