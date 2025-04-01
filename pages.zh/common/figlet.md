# figlet

> 从用户输入生成 ASCII 标语。
> 另请参见: `showfigfonts`。
> 更多信息: <http://www.figlet.org/figlet-man.html>。

- 通过直接输入文本生成：

`figlet {{input_text}}`

- 使用自定义 [f]ont 字体文件：

`figlet {{input_text}} -f {{path/to/font_file.flf}}`

- 使用默认字体目录中的 [f]ont 字体（可以省略扩展名）：

`figlet {{input_text}} -f {{font_filename}}`

- 通过 FIGlet 管道命令输出：

`{{command}} | figlet`

- 显示可用的 FIGlet 字体：

`showfigfonts {{optional_string_to_display}}`

- 使用终端的全宽并居中显示输入文本：

`figlet -t -c {{input_text}}`

- 以全 [W]idth 宽度显示所有字符以避免重叠：

`figlet -W {{input_text}}`
