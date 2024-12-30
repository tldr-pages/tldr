# libtoolize

> 一个用于准备包以使用 `libtool` 的 `autotools` 工具。
> 它执行各种任务，包括生成必要的文件和目录，以将 `libtool` 无缝集成到项目中。
> 更多信息：<https://www.gnu.org/software/libtool/manual/libtool.html#Invoking-libtoolize>。

- 通过复制必要的文件（避免符号链接）并在需要时覆盖现有文件来初始化一个用于 `libtool` 的项目：

`libtoolize --copy --force`