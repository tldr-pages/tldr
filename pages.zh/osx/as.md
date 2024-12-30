# as

> 可移植的GNU汇编器。
> 主要用于将`gcc`的输出汇编为`ld`使用。
> 更多信息：<https://keith.github.io/xcode-man-pages/as.1.html>。

- 汇编一个文件，将输出写入`a.out`：

`as {{path/to/file.s}}`

- 将输出汇编到指定文件：

`as {{path/to/file.s}} -o {{path/to/output_file.o}}`

- 通过跳过空白和注释预处理来加快输出生成速度。（仅应对受信任的编译器使用）：

`as -f {{path/to/file.s}}`

- 将给定路径包含在搜索`.include`指令中指定文件的目录列表中：

`as -I {{path/to/directory}} {{path/to/file.s}}`