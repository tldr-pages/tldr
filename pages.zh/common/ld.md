# ld

> 链接目标文件。
> 更多信息：<https://sourceware.org/binutils/docs-2.38/ld.html>.

- 链接一个特定的目标文件（没有依赖关系）生成可执行文件：

`ld {{path/to/file.o}} --output {{path/to/output_executable}}`

- 链接两个目标文件生成一个可执行文件：

`ld {{path/to/file1.o}} {{path/to/file2.o}} --output {{path/to/output_executable}}`

- 动态链接 x86_64 程序到 glibc（文件路径根据系统而变化）：

`ld --output {{path/to/output_executable}} --dynamic-linker /lib/ld-linux-x86-64.so.2 /lib/crt1.o /lib/crti.o -lc {{path/to/file.o}} /lib/crtn.o`
