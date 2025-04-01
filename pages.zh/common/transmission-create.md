# transmission-create

> 创建 BitTorrent `.torrent` 文件。
> 参见：`transmission`。
> 更多信息：<https://manned.org/transmission-create>.

- 创建一个每个分段大小为 2048 KB 的种子文件：

`transmission-create -o {{path/to/example.torrent}} --tracker {{tracker_announce_url}} --piecesize {{2048}} {{path/to/file_or_directory}}`

- 创建一个私有种子文件，每个分段大小为 2048 KB：

`transmission-create -p -o {{path/to/example.torrent}} --tracker {{tracker_announce_url}} --piecesize {{2048}} {{path/to/file_or_directory}}`

- 创建一个带注释的种子文件：

`transmission-create -o {{path/to/example.torrent}} --tracker {{tracker_url1}} -c {{comment}} {{path/to/file_or_directory}}`

- 创建一个包含多个追踪器的种子文件：

`transmission-create -o {{path/to/example.torrent}} --tracker {{tracker_url1}} --tracker {{tracker_url2}} {{path/to/file_or_directory}}`

- 显示帮助页面：

`transmission-create --help`
