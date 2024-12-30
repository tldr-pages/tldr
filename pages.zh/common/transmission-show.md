# transmission-show

> 获取有关种子文件的信息。
> 另请参见：`transmission`。
> 更多信息：<https://manned.org/transmission-show>。

- 显示特定种子的元数据：

`transmission-show {{path/to/file.torrent}}`

- 为特定种子生成磁力链接：

`transmission-show --magnet {{path/to/file.torrent}}`

- 查询种子的跟踪器并打印当前的对等节点数量：

`transmission-show --scrape {{path/to/file.torrent}}`