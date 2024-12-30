# base64

> 编码或解码文件或 `stdin` 到/从 base64，输出到 `stdout` 或另一个文件。
> 更多信息：<https://keith.github.io/xcode-man-pages/base64.1.html>。

- 将文件编码到 `stdout`：

`base64 {{-i|--input}} {{path/to/file}}`

- 将文件编码到指定的输出文件：

`base64 {{-i|--input}} {{path/to/input_file}} {{-o|--output}} {{path/to/output_file}}`

- 在特定宽度下换行编码输出（`0` 禁用换行）：

`base64 {{-b|--break}} {{0|76|...}} {{path/to/file}}`

- 将文件解码到 `stdout`：

`base64 {{-d|--decode}} {{-i|--input}} {{path/to/file}}`

- 从 `stdin` 编码到 `stdout`：

`{{command}} | base64`

- 从 `stdin` 解码到 `stdout`：

`{{command}} | base64 {{-d|--decode}}`