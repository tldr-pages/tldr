# od

> 以八进制、十进制或十六进制格式显示文件内容。
> 可选择性地显示每行的字节偏移量和/或可打印表示。
> 更多信息：<https://www.gnu.org/software/coreutils/od>。

- 使用默认设置显示文件：八进制格式，每行8个字节，八进制字节偏移量，重复行用 `*` 替代：

`od {{path/to/file}}`

- 以详细模式显示文件，即不用 `*` 替代重复行：

`od -v {{path/to/file}}`

- 以十六进制格式显示文件（2字节单位），字节偏移量为十进制格式：

`od --format={{x}} --address-radix={{d}} -v {{path/to/file}}`

- 以十六进制格式显示文件（1字节单位），每行4个字节：

`od --format={{x1}} --width={{4}} -v {{path/to/file}}`

- 以十六进制格式显示文件及其字符表示，并且不打印字节偏移量：

`od --format={{xz}} --address-radix={{n}} -v {{path/to/file}}`

- 从第500个字节开始只读取文件的100个字节：

`od --read-bytes 100 --skip-bytes=500 -v {{path/to/file}}`