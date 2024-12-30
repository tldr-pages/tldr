# fold

> 将输入文件中的每一行包装以适应指定的宽度，并将其打印到`stdout`。
> 更多信息：<https://manned.org/fold.1p>。

- 将每一行包装到默认宽度（80个字符）：

`fold {{path/to/file}}`

- 将每一行包装到宽度“30”：

`fold -w30 {{path/to/file}}`

- 将每一行包装到宽度“5”，并在空格处换行（将每个以空格分隔的单词放在新的一行中，长度超过5的单词会被包装）：

`fold -w5 -s {{path/to/file}}`