# fold

> 将输入文件中的每一行调整为指定宽度，并打印到 `stdout`。
> 更多信息：<https://manned.org/fold.1p>。

- 将每一行调整为默认宽度（80个字符）：

`fold {{path/to/file}}`

- 将每一行调整为宽度“30”：

`fold -w30 {{path/to/file}}`

- 将每一行调整为宽度“5”，并在空格处断行（每个用空格分隔的词将占据新的一行，长度超过5的词会被拆分）：

`fold -w5 -s {{path/to/file}}`