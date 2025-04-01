# transmission-show

> 获取关于 torrent 文件的信息。
> 参见：`transmission`。
> 更多信息：<https://manned.org/transmission-show>。

- 显示特定 torrent 的元数据：

`transmission-show {{path/to/file.torrent}}`

- 为特定 torrent 生成磁力链接：

`transmission-show --magnet {{path/to/file.torrent}}`

- 查询 torrent 的跟踪器并打印当前的对等节点数量：

`transmission-show --scrape {{path/to/file.torrent}}`
