# nkf

> 网络汉字过滤器：将汉字编码从一种编码转换为另一种编码。
> 更多信息：<https://manned.org/nkf>.

- 将文件转换为 UTF-8 编码：

`nkf -w {{path/to/file.txt}}`

- 将文件转换为 SHIFT_JIS 编码：

`nkf -s {{path/to/file.txt}}`

- 将文件转换为 UTF-8 编码并覆盖原文件：

`nkf -w --overwrite {{path/to/file.txt}}`

- 使用 LF 作为新行代码并覆盖（UNIX 类型）：

`nkf -d --overwrite {{path/to/file.txt}}`

- 使用 CRLF 作为新行代码并覆盖（Windows 类型）：

`nkf -c --overwrite {{path/to/file.txt}}`

- 解码 MIME 文件并覆盖：

`nkf -m --overwrite {{path/to/file.txt}}`