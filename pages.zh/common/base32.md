# base32

> 将文件或 `stdin` 编码或解码为 Base32，输出到 `stdout`。
> 更多信息：<https://manned.org/base32>。

- 编码文件：

`base32 {{path/to/file}}`

- 在特定宽度处换行编码输出（`0` 禁用换行）：

`base32 {{-w|--wrap}} {{0|76|...}} {{path/to/file}}`

- 解码文件：

`base32 {{-d|--decode}} {{path/to/file}}`

- 从 `stdin` 编码：

`{{command}} | base32`

- 从 `stdin` 解码：

`{{command}} | base32 {{-d|--decode}}`