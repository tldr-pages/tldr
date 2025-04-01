# libtoolize

> 一个 `autotools` 工具，用于使软件包支持 `libtool`。
> 它执行各种任务，包括生成必要的文件和目录，以便将 `libtool` 无缝集成到项目中。
> 更多信息：<https://www.gnu.org/software/libtool/manual/libtool.html#Invoking-libtoolize>。

- 通过复制必要的文件（避免符号链接）并根据需要覆盖现有文件来初始化 `libtool` 项目：

`libtoolize {{[-c|--copy]}} {{[-f|--force]}}`
