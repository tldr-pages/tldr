# tarsnap

> 操作远程 Tarsnap 加密备份。
> 注意：如果您在 `/usr/local/etc/tarsnap.conf` 或 `~/.tarsnaprc` 中配置了密钥文件和缓存目录，则不需要指定它们。
> 另见：`tarsnap-keygen`。
> 更多信息：<https://www.tarsnap.com/man-tarsnap.1.html>。

- [c]reate 备份一个或多个文件或目录，指定加密密钥和缓存目录：

`tarsnap -c --keyfile {{path/to/key_file}} --cachedir {{path/to/cache_directory}} -f {{archive_name}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 显示将要上传的数据量：

`tarsnap -c --dry-run --print-stats --keyfile {{path/to/key_file}} --cachedir {{path/to/cache_directory}} -f {{archive_name}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 列出已存档的文件：

`tarsnap --list-archives --keyfile {{path/to/key_file}}`

- [d]elete 删除特定的存档：

`tarsnap -d --keyfile {{path/to/key_file}} --cachedir {{path/to/cache_directory}} -f {{archive_name}}`

- Lis[t] 在 [v]erbose 模式下列出特定存档的内容：

`tarsnap -tv --keyfile {{path/to/key_file}} -f {{archive_name}}`

- 从特定存档恢复一个或多个文件或目录：

`tarsnap -x --keyfile {{path/to/key_file}} -f {{archive_name}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 复制存档：

`tarsnap -c --keyfile {{path/to/key_file}} -f {{new_archive_name}} @@{{source_archive_name}}`