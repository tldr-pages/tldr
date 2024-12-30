# zip

> 将文件压缩成 Zip 归档。
> 另见：`unzip`。
> 更多信息：<https://manned.org/zip>。

- 将文件/目录添加到指定归档：

`zip -r {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 从指定归档中删除文件/目录：

`zip --delete {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 归档文件/目录，但排除指定的文件/目录：

`zip {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}} --exclude {{path/to/excluded_files_or_directories}}`

- 以特定压缩级别归档文件/目录（`0` - 最低，`9` - 最高）：

`zip -r -{{0..9}} {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 创建一个带有特定密码的加密归档：

`zip -r --encrypt {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 将文件/目录归档为多部分 [s]plit Zip 归档（例如 3 GB 的部分）：

`zip -r -s {{3g}} {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 打印特定归档的内容：

`zip -sf {{path/to/compressed.zip}}`