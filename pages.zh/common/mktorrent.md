# mktorrent

> 创建 BitTorrent 元信息文件。
> 更多信息：<https://github.com/Rudde/mktorrent>。

- 创建一个块大小为 2^21 KB 的 torrent：

`mktorrent -a {{tracker_announce_url}} -l {{21}} -o {{path/to/example.torrent}} {{path/to/file_or_directory}}`

- 创建一个块大小为 2^21 KB 的私有 torrent：

`mktorrent -p -a {{tracker_announce_url}} -l {{21}} -o {{path/to/example.torrent}} {{path/to/file_or_directory}}`

- 创建一个带有注释的 torrent：

`mktorrent -c "{{comment}}" -a {{tracker_announce_url}} -l {{21}} -o {{path/to/example.torrent}} {{path/to/file_or_directory}}`

- 创建一个带有多个 tracker 的 torrent：

`mktorrent -a {{tracker_announce_url,tracker_announce_url_2}} -l {{21}} -o {{path/to/example.torrent}} {{path/to/file_or_directory}}`

- 创建一个带有网页种子 URL 的 torrent：

`mktorrent -a {{tracker_announce_url}} -w {{web_seed_url}} -l {{21}} -o {{path/to/example.torrent}} {{path/to/file_or_directory}}`