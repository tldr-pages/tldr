# cppcheck

> 一个用于 C/C++ 代码的静态分析工具。
> 它不仅关注语法错误，还专注于编译器通常无法检测到的各种错误类型。
> 更多信息：<https://cppcheck.sourceforge.net>。

- 递归检查当前目录，显示进度并将错误消息记录到文件中：

`cppcheck . 2> cppcheck.log`

- 递归检查给定目录，不打印进度消息：

`cppcheck --quiet {{path/to/directory}}`

- 检查给定文件，指定要执行的测试（默认情况下只显示错误）：

`cppcheck --enable {{error|warning|style|performance|portability|information|all}} {{path/to/file.cpp}}`

- 列出可用测试：

`cppcheck --errorlist`

- 检查给定文件，忽略特定测试：

`cppcheck --suppress {{test_id1}} --suppress {{test_id2}} {{path/to/file.cpp}}`

- 检查当前目录，提供外部包含文件的路径（例如，外部库）：

`cppcheck -I {{include/directory_1}} -I {{include/directory_2}} .`

- 检查 Microsoft Visual Studio 项目（`*.vcxproj`）或解决方案（`*.sln`）：

`cppcheck --project {{path/to/project.sln}}`