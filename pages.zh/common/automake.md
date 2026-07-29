# automake

> 为使用 GNU 标准的软件项目自动生成 Makefile。
> 更多信息：<https://www.gnu.org/software/automake/manual/automake.html#automake-Invocation>。

- 运行 automake 在编辑 `Makefile.am` 后重新生成 Makefile：

`automake`

- 为非 GNU 项目生成 `Makefile.in`（foreign 模式）：

`automake --foreign`

- 添加详细输出以进行调试：

`automake {{[-v|--verbose]}}`

- 添加缺失的标准文件（INSTALL、COPYING、depcomp 等）：

`automake {{[-a|--add-missing]}}`

- 显示帮助信息：

`automake --help`
