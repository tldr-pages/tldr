# pygmentize

> 基于 Python 的语法高亮工具。
> 更多信息：<https://pygments.org/docs/cmdline/>.

- 高亮文件的语法并输出至 `stdout`（语言从文件扩展名推断）：

`pygmentize {{file.py}}`

- 显式设置语法高亮使用的语言：

`pygmentize -l {{javascript}} {{input_file}}`

- 列出可用的词法分析器（输入语言处理程序）：

`pygmentize -L lexers`

- 将输出保存为 HTML 格式的文件：

`pygmentize -f html -o {{output_file.html}} {{input_file.py}}`

- 列出可用的输出格式：

`pygmentize -L formatters`

- 生成 HTML 文件，包含额外的格式化选项（完整页面，带行号）：

`pygmentize -f html -O "full,linenos=True" -o {{output_file.html}} {{input_file}}`