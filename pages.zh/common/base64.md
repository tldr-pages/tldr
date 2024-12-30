# base64

> 将文件或 `stdin` 编码或解码为 base64，输出到 `stdout`。
> 更多信息：<https://manned.org/base64>。

- 编码文件：

`base64 {{path/to/file}}`

- 在特定宽度下包装编码输出（`0` 禁用包装）：

`base64 {{-w|--wrap}} {{0|76|...}} {{path/to/file}}`

- 解码文件：

`base64 {{-d|--decode}} {{path/to/file}}`

- 从 `stdin` 编码：

`{{command}} | base64`

- 从 `stdin` 解码：

`{{command}} | base64 {{-d|--decode}}`