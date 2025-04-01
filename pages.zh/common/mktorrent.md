# mktorrent

> 创建 BitTorrent 元信息文件。
> 更多信息：<https://github.com/Rudde/mktorrent>.

- 创建一个每个分片大小为 2^21 KB 的种子文件：

`mktorrent -a {{tracker_announce_url}} -l {{21}} -o {{path/to/example.torrent}} {{path/to/file_or_directory}}`

- 创建一个私有种子文件，每个分片大小为 2^21 KB：

`mktorrent -p -a {{tracker_announce_url}} -l {{21}} -o {{path/to/example.torrent}} {{path/to/file_or_directory}}`

- 创建一个带有注释的种子文件：

`mktorrent -c "{{comment}}" -a {{tracker_announce_url}} -l {{21}} -o {{path/to/example.torrent}} {{path/to/file_or_directory}}`

- 创建一个带有多个追踪器的种子文件：

`mktorrent -a {{tracker_announce_url,tracker_announce_url_2}} -l {{21}} -o {{path/to/example.torrent}} {{path/to/file_or_directory}}`

- 创建一个带有 Web 种子 URL 的种子文件：

`mktorrent -a {{tracker_announce_url}} -w {{web_seed_url}} -l {{21}} -o {{path/to/example.torrent}} {{path/to/file_or_directory}}`