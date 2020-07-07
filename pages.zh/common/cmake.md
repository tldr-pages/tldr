# cmake

> 跨平台构建系统生成器。
> 它会根据目标系统生成 Makefile，Visual Studio 项目或其他。
> 更多信息： <https://cmake.org/cmake/help/v3.2/manual/cmake.1.html>.

- Generate a Makefile and use it to compile a project in the same directory as the source:

`cmake && make`

- 生成一个 Makefile 并将其用于在单独的 "build" 目录（在源代码外构建）中编译项目：

`cmake -H. -B{{build}} && make -C {{build}}`
