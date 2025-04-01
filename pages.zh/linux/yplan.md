# yplan

> 为选定的任意年份生成两页竖向的日常计划表的 LaTeX 代码。
> 生成的输出可以使用 `pandoc`、`pdflatex` 或 `xetex` 等转换工具进行转换或打印。
> 更多信息：<https://www.ctan.org/tex-archive/macros/latex/contrib/yplan>.

- 创建指定语言、大小写（大写或小写）和年份的日常计划表：

`yplan {{language}} {{lettercase}} {{year}} > {{path/to/file.tex}}`