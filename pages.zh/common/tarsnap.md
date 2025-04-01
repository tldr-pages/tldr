# tarsnap

> 操作远程 Tarsnap 加密备份。
> 注意：如果在 `/usr/local/etc/tarsnap.conf` 或 `~/.tarsnaprc` 中配置了密钥文件和缓存目录，则无需指定。
> 另见：`tarsnap-keygen`。
> 更多信息：<https://www.tarsnap.com/man-tarsnap.1.html>。

- [c]创建一个或多个文件或目录的备份存档，并指定加密密钥和缓存目录：

`tarsnap -c --keyfile {{path/to/key_file}} --cachedir {{path/to/cache_directory}} -f {{archive_name}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 显示将上传的数据量：

`tarsnap -c --dry-run --print-stats --keyfile {{path/to/key_file}} --cachedir {{path/to/cache_directory}} -f {{archive_name}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 列出存储的存档：

`tarsnap --list-archives --keyfile {{path/to/key_file}}`

- [d]删除特定的存档：

`tarsnap -d --keyfile {{path/to/key_file}} --cachedir {{path/to/cache_directory}} -f {{archive_name}}`

- 以[v]详细模式列出特定存档的内容：

`tarsnap -tv --keyfile {{path/to/key_file}} -f {{archive_name}}`

- 从特定存档中恢复一个或多个文件或目录：

`tarsnap -x --keyfile {{path/to/key_file}} -f {{archive_name}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 复制存档：

`tarsnap -c --keyfile {{path/to/key_file}} -f {{new_archive_name}} @@{{source_archive_name}}`
