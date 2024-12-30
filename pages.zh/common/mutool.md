# mutool

> 转换、查询信息并提取PDF文件中的数据。
> 更多信息：<https://mupdf.readthedocs.io/en/latest/mupdf-command-line.html>。

- 将指定范围的页面转换为PNG格式（注意：输出占位符中的`%nd`必须替换为打印修饰符，如`%d`或`%2d`）：

`mutool convert -o {{path/to/output%nd.png}} {{path/to/input.pdf}} {{1-10}}`

- 将一个或多个PDF页面转换为`stdout`中的文本：

`mutool draw -F txt {{path/to/input.pdf}} {{2,3,5,...}}`

- 合并多个PDF文件：

`mutool merge -o {{path/to/output.pdf}} {{path/to/input1.pdf path/to/input2.pdf ...}}`

- 查询有关PDF中所有嵌入内容的信息：

`mutool info {{path/to/input.pdf}}`

- 将PDF中嵌入的所有图像、字体和资源提取到当前目录：

`mutool extract {{path/to/input.pdf}}`

- 显示PDF的目录（大纲）：

`mutool show {{path/to/input.pdf}} outline`