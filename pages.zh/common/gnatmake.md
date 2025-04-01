# gnatmake

> 用于 Ada 程序的底层构建工具（GNAT 工具链的一部分）。
> 更多信息：<https://gcc.gnu.org/onlinedocs/gnat_ugn/Switches-for-gnatmake.html>.

- 编译可执行文件:

`gnatmake {{source_file1.adb source_file2.adb ...}}`

- 设置自定义的可执行文件名:

`gnatmake -o {{executable_name}} {{source_file.adb}}`

- [f]强制重新编译:

`gnatmake -f {{source_file.adb}}`
