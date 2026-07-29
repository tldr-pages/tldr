# od

> 以八进制、十进制或十六进制格式显示文件内容。
> 可选显示每行的字节偏移量和/或可打印字符表示。
> 另请参阅：`hexyl`、`xxd`、`hexdump`。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/od-invocation.html>。

- 以默认设置显示文件：八进制格式，每行 8 字节，八进制字节偏移量，重复行替换为 `*`：

`od {{路径/到/文件}}`

- 以详细模式显示文件，即不替换重复行：

`od {{[-v|--output-duplicates]}} {{路径/到/文件}}`

- 以十六进制格式（2 字节单位）和十进制字节偏移量显示文件：

`od {{[-t|--format]}} {{x}} {{[-A|--address-radix]}} {{d}} {{[-v|--output-duplicates]}} {{路径/到/文件}}`

- 以十六进制格式（1 字节单位）和每行 4 字节显示文件：

`od {{[-t|--format]}} {{x1}} {{[-w|--width=]}}4 {{[-v|--output-duplicates]}} {{路径/到/文件}}`

- 以十六进制格式及其字符表示显示文件，不打印字节偏移量：

`od {{[-t|--format]}} {{xz}} {{[-A|--address-radix]}} {{n}} {{[-v|--output-duplicates]}} {{路径/到/文件}}`

- 从第 500 个字节开始读取文件的 100 个字节：

`od {{[-N|--read-bytes]}} 100 {{[-j|--skip-bytes]}} 500 {{[-v|--output-duplicates]}} {{路径/到/文件}}`
