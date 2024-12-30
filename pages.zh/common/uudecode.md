# uudecode

> 解码由 `uuencode` 编码的文件。
> 更多信息： <https://manned.org/uudecode>。

- 解码一个使用 `uuencode` 编码的文件，并将结果打印到 `stdout`：

`uudecode {{path/to/encoded_file}}`

- 解码一个使用 `uuencode` 编码的文件，并将结果写入文件：

`uudecode -o {{path/to/decoded_file}} {{path/to/encoded_file}}`