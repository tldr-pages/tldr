# uuencode

> 将二进制文件编码为 ASCII，以便通过仅支持简单 ASCII 编码的媒介进行传输。
> 更多信息：<https://manned.org/uuencode>。

- 编码一个文件并将结果打印到 `stdout`：

`uuencode {{path/to/input_file}} {{output_file_name_after_decoding}}`

- 编码一个文件并将结果写入文件：

`uuencode -o {{path/to/output_file}} {{path/to/input_file}} {{output_file_name_after_decoding}}`

- 使用 Base64 编码文件而不是默认的 uuencode 编码，并将结果写入文件：

`uuencode -m -o {{path/to/output_file}} {{path/to/input_file}} {{output_file_name_after_decoding}}`