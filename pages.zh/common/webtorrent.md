# webtorrent

> WebTorrent 的命令行接口。
> 支持磁力链接、URL、信息哈希和 `.torrent` 文件。
> 更多信息：<https://github.com/webtorrent/webtorrent-cli>。

- 下载一个种子文件：

`webtorrent download "{{torrent_id}}"`

- 将种子文件流媒体传输到 VLC 媒体播放器：

`webtorrent download "{{torrent_id}}" --vlc`

- 将种子文件流媒体传输到 Digital Living Network Alliance (DLNA) 设备：

`webtorrent download "{{torrent_id}}" --dlna`

- 显示特定种子文件的文件列表：

`webtorrent download "{{torrent_id}}" --select`

- 指定要下载的种子文件中的文件索引：

`webtorrent download "{{torrent_id}}" --select {{index}}`

- 分享特定的文件或目录：

`webtorrent seed {{path/to/file_or_directory}}`

- 为指定的文件路径创建新的种子文件：

`webtorrent create {{path/to/file}}`

- 显示磁力链接或 `.torrent` 文件的信息：

`webtorrent info {{path/to/file_or_magnet}}`