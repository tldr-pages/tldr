# webtorrent

> WebTorrent 的命令行界面。
> 支持磁链、网址、信息哈希和 `.torrent` 文件。
> 更多信息：<https://github.com/webtorrent/webtorrent-cli>。

- 下载一个 torrent：

`webtorrent download "{{torrent_id}}"`

- 将 torrent 流媒体播放到 VLC 媒体播放器：

`webtorrent download "{{torrent_id}}" --vlc`

- 将 torrent 流媒体播放到数字生活网络联盟 (DLNA) 设备：

`webtorrent download "{{torrent_id}}" --dlna`

- 显示特定 torrent 的文件列表：

`webtorrent download "{{torrent_id}}" --select`

- 指定要下载的 torrent 文件索引：

`webtorrent download "{{torrent_id}}" --select {{index}}`

- 共享特定文件或目录：

`webtorrent seed {{path/to/file_or_directory}}`

- 为指定的文件路径创建一个新的 torrent 文件：

`webtorrent create {{path/to/file}}`

- 显示磁链 URI 或 `.torrent` 文件的信息：

`webtorrent info {{path/to/file_or_magnet}}`