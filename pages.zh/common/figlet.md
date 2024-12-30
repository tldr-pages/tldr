# figlet

> 从用户输入生成ASCII横幅。
> 另见：`showfigfonts`。
> 更多信息：<http://www.figlet.org/figlet-man.html>。

- 通过直接输入文本生成：

`figlet {{input_text}}`

- 使用自定义[f]ont文件：

`figlet {{input_text}} -f {{path/to/font_file.flf}}`

- 使用默认字体目录中的[f]ont（可以省略扩展名）：

`figlet {{input_text}} -f {{font_filename}}`

- 将命令输出通过FIGlet管道传输：

`{{command}} | figlet`

- 显示可用的FIGlet字体：

`showfigfonts {{optional_string_to_display}}`

- 使用[t]erminal的全宽并[c]enter输入文本：

`figlet -t -c {{input_text}}`

- 以全[W]idth显示所有字符以避免重叠：

`figlet -W {{input_text}}`