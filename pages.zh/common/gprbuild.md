# gprbuild

> 一种用于用Ada和其他语言（C/C++/Fortran）编写项目的高级构建工具。
> 更多信息：<https://docs.adacore.com/gprbuild-docs/html/gprbuild_ug.html>。

- 构建项目（假设当前目录中仅存在一个 `*.gpr` 文件）：

`gprbuild`

- 构建特定的 [P]roject 文件：

`gprbuild -P{{project_name}}`

- 清理构建工作区：

`gprclean`

- 安装编译后的二进制文件：

`gprinstall --prefix {{path/to/installation/dir}}`