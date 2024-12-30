# gzip

> 使用 `gzip` 压缩（LZ77）压缩文件/解压缩文件。
> 更多信息请访问：<https://www.gnu.org/software/gzip/manual/gzip.html>。

- 压缩一个文件，并用 `gzip` 归档替换它：

`gzip {{path/to/file}}`

- 解压缩一个文件，并用原始未压缩版本替换它：

`gzip {{-d|--decompress}} {{path/to/file.gz}}`

- 压缩一个文件，保留原始文件：

`gzip {{-k|--keep}} {{path/to/file}}`

- 压缩一个文件，指定输出文件名：

`gzip {{-c|--stdout}} {{path/to/file}} > {{path/to/compressed_file.gz}}`

- 解压缩一个 `gzip` 归档，指定输出文件名：

`gzip {{-c|--stdout}} {{-d|--decompress}} {{path/to/file.gz}} > {{path/to/uncompressed_file}}`

- 指定压缩级别。1 是最快（低压缩），9 是最慢（高压缩），6 是默认值：

`gzip -{{1..9}} {{-c|--stdout}} {{path/to/file}} > {{path/to/compressed_file.gz}}`

- 显示每个压缩或解压缩文件的名称和减少百分比：

`gzip {{-v|--verbose}} {{-d|--decompress}} {{path/to/file.gz}}`