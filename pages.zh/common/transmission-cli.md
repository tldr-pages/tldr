# transmission-cli

> 一个轻量级的命令行 BitTorrent 客户端。
> 该工具已被弃用，请参见 `transmission-remote`。
> 更多信息：<https://transmissionbt.com>。

- 下载特定的种子：

`transmission-cli {{url|magnet|path/to/file}}`

- 下载种子到特定目录：

`transmission-cli --download-dir {{path/to/download_directory}} {{url|magnet|path/to/file}}`

- 从特定文件或目录创建种子文件：

`transmission-cli --new {{path/to/source_file_or_directory}}`

- 指定下载速度限制（以 KB/s 为单位）：

`transmission-cli --downlimit {{50}} {{url|magnet|path/to/file}}`

- 指定上传速度限制（以 KB/s 为单位）：

`transmission-cli --uplimit {{50}} {{url|magnet|path/to/file}}`

- 使用特定端口进行连接：

`transmission-cli --port {{port_number}} {{url|magnet|path/to/file}}`

- 强制加密对等连接：

`transmission-cli --encryption-required {{url|magnet|path/to/file}}`

- 使用 Bluetack 格式的对等阻止列表：

`transmission-cli --blocklist {{blocklist_url|path/to/blocklist}} {{url|magnet|path/to/file}}`