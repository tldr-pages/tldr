# cppcheck

> 一个用于 C/C++ 代码的静态分析工具。
> 而不是检查语法错误，它专注于编译器通常不会检测到的 bug 类型。
> 更多信息：<https://cppcheck.sourceforge.net>。

- 递归检查当前目录，显示屏幕上的进度并记录错误信息到文件：

`cppcheck . 2> cppcheck.log`

- 递归检查指定目录，不显示进度消息：

`cppcheck --quiet {{path/to/directory}}`

- 检查指定文件，指定要执行的测试（默认仅显示错误）：

`cppcheck --enable {{error|warning|style|performance|portability|information|all}} {{path/to/file.cpp}}`

- 列出可用的测试：

`cppcheck --errorlist`

- 检查指定文件，忽略特定的测试：

`cppcheck --suppress {{test_id1}} --suppress {{test_id2}} {{path/to/file.cpp}}`

- 检查当前目录，提供位于该目录之外的包含文件的路径（例如外部库）：

`cppcheck -I {{include/directory_1}} -I {{include/directory_2}} .`

- 检查 Microsoft Visual Studio 项目（`*.vcxproj`）或解决方案（`*.sln`）：

`cppcheck --project {{path/to/project.sln}}`