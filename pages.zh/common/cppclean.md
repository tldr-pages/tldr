# cppclean

> 在 C++ 项目中查找未使用的代码。
> 更多信息：<https://github.com/myint/cppclean>.

- 在项目的目录中运行：

`cppclean {{path/to/project}}`

- 在项目中运行，其中头文件位于 `inc1/` 和 `inc2/` 目录中：

`cppclean {{path/to/project}} --include-path {{inc1}} --include-path {{inc2}}`

- 在特定文件 `main.cpp` 上运行：

`cppclean {{main.cpp}}`

- 在当前目录中运行，排除 "build" 目录：

`cppclean {{.}} --exclude {{build}}`