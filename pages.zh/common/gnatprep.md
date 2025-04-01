# gnatprep

> 用于 Ada 源代码文件的预处理器（GNAT 工具链的一部分）。
> 更多信息：<https://gcc.gnu.org/onlinedocs/gnat_ugn/Preprocessing-with-gnatprep.html>。

- 从文件中使用符号定义：

`gnatprep {{source_file}} {{target_file}} {{definitions_file}}`

- 在命令行中指定符号值：

`gnatprep -D{{name}}={{value}} {{source_file}} {{target_file}}`