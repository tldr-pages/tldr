# 7za

> 一个具有高压缩比的文件归档工具。
> 类似于 `7z`，但支持的文件类型较少且是跨平台的。
> 更多信息：<https://manned.org/7za>。

- [a] 归档一个文件或目录：

`7za a {{path/to/archive.7z}} {{path/to/file_or_directory}}`

- 加密现有的归档文件（包括文件名）：

`7za a {{path/to/encrypted.7z}} -p{{password}} -mhe={{on}} {{path/to/archive.7z}}`

- E[x] 提取一个归档文件，保留原始目录结构：

`7za x {{path/to/archive.7z}}`

- E[x] 提取一个归档文件到特定目录：

`7za x {{path/to/archive.7z}} -o{{path/to/output}}`

- E[x] 将归档文件提取到 `stdout`：

`7za x {{path/to/archive.7z}} -so`

- [a] 使用特定的归档类型进行归档：

`7za a -t{{7z|bzip2|gzip|lzip|tar|...}} {{path/to/archive.7z}} {{path/to/file_or_directory}}`

- [l] 列出归档文件的内容：

`7za l {{path/to/archive.7z}}`

- 设置压缩级别（更高的级别意味着更高的压缩率，但速度更慢）：

`7za a {{path/to/archive.7z}} -mx={{0|1|3|5|7|9}} {{path/to/file_or_directory}}`