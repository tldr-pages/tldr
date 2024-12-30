# as

> 便携式GNU汇编器。
> 主要用于将`gcc`的输出汇编成`ld`使用的格式。
> 更多信息：<https://manned.org/as>。

- 汇编一个文件，将输出写入`a.out`：

`as {{path/to/file.s}}`

- 将输出汇编到指定文件：

`as {{path/to/file.s}} -o {{path/to/output_file.o}}`

- 通过跳过空白和注释预处理来加快输出生成速度。（应仅用于可信编译器）：

`as -f {{path/to/file.s}}`

- 将给定路径包含在搜索`.include`指令中指定的文件的目录列表中：

`as -I {{path/to/directory}} {{path/to/file.s}}`