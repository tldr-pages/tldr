# gnatmake

> 一个用于 Ada 程序的低级构建工具（GNAT 工具链的一部分）。
> 更多信息：<https://gcc.gnu.org/onlinedocs/gnat_ugn/Building-with-gnatmake.html>。

- 编译可执行文件：

`gnatmake {{source_file1.adb source_file2.adb ...}}`

- 设置自定义可执行文件名称：

`gnatmake -o {{executable_name}} {{source_file.adb}}`

- [f]orce 重新编译：

`gnatmake -f {{source_file.adb}}`