# cppcheck

> C/C++ 代码静态分析工具。
> 它关注的不是语法错误，而是编译器通常无法检测到的各类缺陷。
> 更多信息：<https://manned.org/cppcheck>。

- 递归检查当前目录，在屏幕上显示进度，并将错误信息记录到文件：

`cppcheck . 2> cppcheck.log`

- 递归检查指定目录，不打印进度信息：

`cppcheck {{[-q|--quiet]}} {{路径/到/目录}}`

- 检查指定文件，并指定要执行的检查类型（默认仅显示 error 级别）：

`cppcheck --enable {{error|warning|style|performance|portability|information|all}} {{路径/到/文件.cpp}}`

- 列出所有可用的检查类型：

`cppcheck --errorlist`

- 检查指定文件，忽略特定检查项：

`cppcheck --suppress {{检查项ID1}} --suppress {{检查项ID2}} {{路径/到/文件.cpp}}`

- 检查当前目录，并为其外部的头文件指定搜索路径（例如外部库）：

`cppcheck -I {{头文件目录1}} -I {{头文件目录2}} .`

- 检查 Microsoft Visual Studio 项目（`*.vcxproj`）或解决方案（`*.sln`）：

`cppcheck --project {{路径/到/项目.sln}}`
