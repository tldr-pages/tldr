# objcopy

> 将对象文件的内容复制到另一个文件。
> 更多信息：<https://manned.org/objcopy>。

- 将数据复制到另一个文件：

`objcopy {{path/to/source_file}} {{path/to/target_file}}`

- 将对象文件从一种格式转换为另一种格式：

`objcopy --input-target={{input_format}} --output-target {{output_format}} {{path/to/source_file}} {{path/to/target_file}}`

- 从文件中删除所有符号信息：

`objcopy --strip-all {{path/to/source_file}} {{path/to/target_file}}`

- 从文件中删除调试信息：

`objcopy --strip-debug {{path/to/source_file}} {{path/to/target_file}}`

- 从源文件中复制特定部分到目标文件：

`objcopy --only-section {{section}} {{path/to/source_file}} {{path/to/target_file}}`
