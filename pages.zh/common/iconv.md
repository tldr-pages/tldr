# iconv

> 将文本从一种编码转换为另一种编码。
> 更多信息：<https://manned.org/iconv>.

- 将文件转换为指定编码，并输出到 `stdout`：

`iconv -f {{from_encoding}} -t {{to_encoding}} {{input_file}}`

- 将文件转换为当前区域设置的编码，并输出到文件：

`iconv -f {{from_encoding}} {{input_file}} > {{output_file}}`

- 列出支持的编码：

`iconv -l`
