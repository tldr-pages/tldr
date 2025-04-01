# split

> 将文件分割成多个部分。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/split-invocation.html>.

- 将文件分割，每个分割文件包含10行（最后一个分割文件除外）：

`split {{[-l|--lines]}} 10 {{path/to/file}}`

- 将文件分割成5个文件。文件分割为每个分割文件大小相同（最后一个分割文件除外）：

`split {{[-n|--number]}} 5 {{path/to/file}}`

- 将文件分割，每个分割文件包含512字节（最后一个分割文件除外；使用512k表示千字节，512m表示兆字节）：

`split {{[-b|--bytes]}} 512 {{path/to/file}}`

- 将文件分割，每个分割文件最多包含512字节，且不分割行：

`split {{[-C|--line-bytes]}} 512 {{path/to/file}}`
