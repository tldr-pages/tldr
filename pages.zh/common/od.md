# od

> 以八进制、十进制或十六进制格式显示文件内容。
> 根据需要显示字节偏移量和/或每行的可打印表示。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/od-invocation.html>.

- 使用默认设置显示文件：八进制格式，每行8个字节，字节偏移量以八进制表示，重复行用 `*` 替换：

`od {{path/to/file}}`

- 以详细模式显示文件，即不替换重复行：

`od {{[-v|--output-duplicates]}} {{path/to/file}}`

- 以十六进制格式（2字节单位）显示文件，字节偏移量以十进制格式显示：

`od {{[-t|--format]}} {{x}} {{[-A|--address-radix]}} {{d}} {{[-v|--output-duplicates]}} {{path/to/file}}`

- 以十六进制格式（1字节单位）显示文件，每行4个字节：

`od {{[-t|--format]}} {{x1}} {{[-w|--width=]}}{{4}} {{[-v|--output-duplicates]}} {{path/to/file}}`

- 以十六进制格式显示文件及其字符表示，不显示字节偏移量：

`od {{[-t|--format]}} {{xz}} {{[-A|--address-radix]}} {{n}} {{[-v|--output-duplicates]}} {{path/to/file}}`

- 从第500字节开始读取100字节的文件内容：

`od {{[-N|--read-bytes]}} 100 {{[-j|--skip-bytes]}} 500 {{[-v|--output-duplicates]}} {{path/to/file}}`
