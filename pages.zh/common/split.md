# split

> 将文件分割成多个部分。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/split-invocation.html>。

- 分割文件，每个部分包含 10 行（最后一个除外）：

`split {{[-l|--lines]}} 10 {{路径/到/文件}}`

- 将文件分割成 5 个文件，每个部分大小相同（最后一个除外）：

`split {{[-n|--number]}} 5 {{路径/到/文件}}`

- 每个部分包含 512 字节（最后一个除外；使用 512k 表示千字节，512m 表示兆字节）：

`split {{[-b|--bytes]}} 512 {{路径/到/文件}}`

- 每个部分最多包含 512 字节，不拆分行：

`split {{[-C|--line-bytes]}} 512 {{路径/到/文件}}`

- 从 `stdin` 分割成多个文件：

`gzip {{[-cd|--stdout --decompress]}} {{路径/到/压缩文件.gz}} | split {{[-l|--lines]}} {{1000}} - {{路径/到/输出}}`
