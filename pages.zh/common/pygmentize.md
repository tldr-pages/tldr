# pygmentize

> 基于Python的语法高亮工具。
> 更多信息请访问：<https://pygments.org/docs/cmdline/>.

- 高亮文件语法并输出到`stdout`（语言从文件扩展名推断）：

`pygmentize {{file.py}}`

- 明确设置语法高亮的语言：

`pygmentize -l {{javascript}} {{input_file}}`

- 列出可用的词法分析器（输入语言的处理器）：

`pygmentize -L lexers`

- 将输出保存为HTML格式的文件：

`pygmentize -f html -o {{output_file.html}} {{input_file.py}}`

- 列出可用的输出格式：

`pygmentize -L formatters`

- 输出一个HTML文件，并带有额外的格式选项（完整页面，带行号）：

`pygmentize -f html -O "full,linenos=True" -o {{output_file.html}} {{input_file}}`