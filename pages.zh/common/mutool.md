# mutool

> 转换、查询信息和从 PDF 文件中提取数据。
> 更多信息：<https://mupdf.readthedocs.io/en/latest/mupdf-command-line.html>.

- 将指定页数范围转换为 PNG 图像（注意：输出占位符中的 `%nd` 必须替换为打印修饰符，例如 `%d` 或 `%2d`）：

`mutool convert -o {{path/to/output%nd.png}} {{path/to/input.pdf}} {{1-10}}`

- 将 PDF 的一个或多个页面转换为文本并输出到 `stdout`：

`mutool draw -F txt {{path/to/input.pdf}} {{2,3,5,...}}`

- 合并多个 PDF 文件：

`mutool merge -o {{path/to/output.pdf}} {{path/to/input1.pdf path/to/input2.pdf ...}}`

- 查询 PDF 中嵌入的所有内容的信息：

`mutool info {{path/to/input.pdf}}`

- 提取 PDF 中嵌入的所有图像、字体和资源到当前目录：

`mutool extract {{path/to/input.pdf}}`

- 显示 PDF 的目录（目录结构）：

`mutool show {{path/to/input.pdf}} outline`
