# Adscript

> Adscript文件的编译器。
> 更多信息：<https://github.com/Amplus2/Adscript>。

- 将文件编译为目标文件：

`adscript --output {{path/to/file.o}} {{path/to/input_file.adscript}}`

- 将文件编译并链接为独立可执行文件：

`adscript --executable --output {{path/to/file}} {{path/to/input_file.adscript}}`

- 将文件编译为LLVM IR而不是本机机器代码：

`adscript --llvm-ir --output {{path/to/file.ll}} {{path/to/input_file.adscript}}`

- 交叉编译文件为外国CPU架构或操作系统的目标文件：

`adscript --target-triple {{i386-linux-elf}} --output {{path/to/file.o}} {{path/to/input_file.adscript}}`