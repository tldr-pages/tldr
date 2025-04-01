# deluge

> 命令行 BitTorrent 客户端。
> 更多信息：<https://deluge-torrent.org>.

- 下载一个 torrent 文件：

`deluge {{url|magnet|path/to/file}}`

- 使用特定的配置文件下载一个 torrent 文件：

`deluge -c {{path/to/configuration_file}} {{url|magnet|path/to/file}}`

- 下载一个 torrent 文件并启动指定的用户界面：

`deluge -u {{gtk|web|console}} {{url|magnet|path/to/file}}`

- 下载一个 torrent 文件并将日志输出到文件：

`deluge -l {{path/to/log_file}} {{url|magnet|path/to/file}}`