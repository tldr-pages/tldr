# transmission-create

> 创建 BitTorrent `.torrent` 文件。
> 另请参见：`transmission`。
> 更多信息：<https://manned.org/transmission-create>。

- 创建一个大小为 2048 KB 的 torrent：

`transmission-create -o {{path/to/example.torrent}} --tracker {{tracker_announce_url}} --piecesize {{2048}} {{path/to/file_or_directory}}`

- 创建一个私有的大小为 2048 KB 的 torrent：

`transmission-create -p -o {{path/to/example.torrent}} --tracker {{tracker_announce_url}} --piecesize {{2048}} {{path/to/file_or_directory}}`

- 创建一个带有注释的 torrent：

`transmission-create -o {{path/to/example.torrent}} --tracker {{tracker_url1}} -c {{comment}} {{path/to/file_or_directory}}`

- 创建一个带有多个 tracker 的 torrent：

`transmission-create -o {{path/to/example.torrent}} --tracker {{tracker_url1}} --tracker {{tracker_url2}} {{path/to/file_or_directory}}`

- 显示帮助页面：

`transmission-create --help`