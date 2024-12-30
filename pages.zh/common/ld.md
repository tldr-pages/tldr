# ld

> 链接目标文件。
> 更多信息：<https://sourceware.org/binutils/docs-2.38/ld.html>。

- 将一个特定的目标文件（没有依赖）链接成可执行文件：

`ld {{path/to/file.o}} --output {{path/to/output_executable}}`

- 将两个目标文件链接在一起：

`ld {{path/to/file1.o}} {{path/to/file2.o}} --output {{path/to/output_executable}}`

- 将 x86_64 程序动态链接到 glibc（文件路径根据系统而异）：

`ld --output {{path/to/output_executable}} --dynamic-linker /lib/ld-linux-x86-64.so.2 /lib/crt1.o /lib/crti.o -lc {{path/to/file.o}} /lib/crtn.o`