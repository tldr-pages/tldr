# zip

> 将文件打包并压缩（归档）到一个 Zip 归档中。
> 另见：`unzip`。
> 更多信息：<https://manned.org/zip>。

- 将文件/目录添加到特定归档中（[r]ecursively）：

`zip -r {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 从特定归档中删除文件/目录（[d]elete）：

`zip -d {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 归档文件/目录，排除指定的文件：

`zip -r {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}} -x {{path/to/excluded_files_or_directories}}`

- 以特定压缩级别归档文件/目录（`0` - 最低，`9` - 最高）：

`zip -r -{{0..9}} {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 使用特定密码创建一个 [e]ncrypted 归档：

`zip -r -e {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 将文件/目录归档为多部分 [s]plit Zip 归档（例如，3 GB 部分）：

`zip -r -s {{3g}} {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 打印特定归档的内容：

`zip -sf {{path/to/compressed.zip}}`