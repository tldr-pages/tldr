# gprbuild

> 一个高级构建工具，用于构建用 Ada 和其他语言（如 C/C++/Fortran）编写的项目。
> 更多信息：<https://docs.adacore.com/gprbuild-docs/html/gprbuild_ug.html>.

- 构建项目（假设当前目录中只有一个 `*.gpr` 文件）:

`gprbuild`

- 构建特定的 [P]roject 文件:

`gprbuild -P{{project_name}}`

- 清理构建工作空间:

`gprclean`

- 安装编译后的二进制文件:

`gprinstall --prefix {{path/to/installation/dir}}`