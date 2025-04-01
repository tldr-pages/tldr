# lpr

> 打印文件。
> 参见：`lpstat` 和 `lpadmin`。
> 更多信息：<https://openprinting.github.io/cups/doc/man-lpr.html>。

- 使用默认打印机打印文件：

`lpr {{path/to/file}}`

- 打印2份：

`lpr -# {{2}} {{path/to/file}}`

- 使用指定名称的打印机打印：

`lpr -P {{printer}} {{path/to/file}}`

- 打印单页（例如：2）或页码范围（例如：2-16）：

`lpr -o page-ranges={{2|2-16}} {{path/to/file}}`

- 双面打印，纵向（长边）或横向（短边）：

`lpr -o sides={{two-sided-long-edge|two-sided-short-edge}} {{path/to/file}}`

- 设置页面大小（根据设置可能有更多选项）：

`lpr -o media={{a4|letter|legal}} {{path/to/file}}`

- 每张纸打印多页：

`lpr -o number-up={{2|4|6|9|16}} {{path/to/file}}`
