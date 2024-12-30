# 字符串

> 在对象文件或二进制文件中查找可打印字符串。
> 更多信息：<https://manned.org/strings>。

- 打印二进制文件中的所有字符串：

`strings {{path/to/file}}`

- 将结果限制为至少 n 个字符长的字符串：

`strings -n {{n}} {{path/to/file}}`

- 在每个结果前加上其在文件中的偏移量：

`strings -t d {{path/to/file}}`

- 在每个结果前加上其在文件中的十六进制偏移量：

`strings -t x {{path/to/file}}`