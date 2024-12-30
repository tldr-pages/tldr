# gnatprep

> Ada源代码文件的预处理器（GNAT工具链的一部分）。
> 更多信息：<https://gcc.gnu.org/onlinedocs/gnat_ugn/Preprocessing-with-gnatprep.html>。

- 从文件中使用符号定义：

`gnatprep {{源文件}} {{目标文件}} {{定义文件}}`

- 在命令行中指定符号值：

`gnatprep -D{{名称}}={{值}} {{源文件}} {{目标文件}}`