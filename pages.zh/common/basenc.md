# basenc

> 使用指定的编码对文件或 `stdin` 进行编码或解码，输出到 `stdout`。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/basenc-invocation.html>。

- 使用 base64 编码对文件进行编码：

`basenc --base64 {{path/to/file}}`

- 使用 base64 编码对文件进行解码：

`basenc --decode --base64 {{path/to/file}}`

- 从 `stdin` 读取并使用 base32 编码（每行 42 列）：

`{{command}} | basenc --base32 -w42`

- 从 `stdin` 读取并使用 base32 编码：

`{{command}} | basenc --base32`