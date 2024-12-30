# 7zr

> 一个具有高压缩比的文件归档工具。
> 类似于 `7z`，但仅支持 7z 文件。
> 更多信息：<https://manned.org/7zr>。

- [a] 归档一个文件或目录：

`7zr a {{path/to/archive.7z}} {{path/to/file_or_directory}}`

- 加密一个现有的归档（包括文件名）：

`7zr a {{path/to/encrypted.7z}} -p{{password}} -mhe={{on}} {{path/to/archive.7z}}`

- E[x] 提取一个归档，保留原始目录结构：

`7zr x {{path/to/archive.7z}}`

- E[x] 提取一个归档到指定目录：

`7zr x {{path/to/archive.7z}} -o{{path/to/output}}`

- E[x] 提取一个归档到 `stdout`：

`7zr x {{path/to/archive.7z}} -so`

- [l] 列出归档的内容：

`7zr l {{path/to/archive.7z}}`

- 设置压缩级别（数字越高，压缩越多，但速度越慢）：

`7zr a {{path/to/archive.7z}} -mx={{0|1|3|5|7|9}} {{path/to/file_or_directory}}`