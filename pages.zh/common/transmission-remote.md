# transmission-remote

> 用于 `transmission-daemon` 和 `transmission` 的远程控制工具。
> 更多信息请访问: <https://transmissionbt.com>。

- 将 torrent 文件或磁力链接添加到 Transmission，并下载到指定目录：

`transmission-remote {{hostname}} -a {{torrent|url}} -w {{/path/to/download_directory}}`

- 更改默认下载目录：

`transmission-remote {{hostname}} -w {{/path/to/download_directory}}`

- 列出所有 torrent：

`transmission-remote {{hostname}} --list`

- 启动 torrent 1 和 2，停止 torrent 3：

`transmission-remote {{hostname}} -t "{{1,2}}" --start -t {{3}} --stop`

- 移除 torrent 1 和 2，并删除 torrent 2 的本地数据：

`transmission-remote {{hostname}} -t {{1}} --remove -t {{2}} --remove-and-delete`

- 停止所有 torrent：

`transmission-remote {{hostname}} -t {{all}} --stop`

- 将 torrent 1-10 和 15-20 移动到一个新目录（如果目录不存在将被创建）：

`transmission-remote {{hostname}} -t "{{1-10,15-20}}" --move {{/path/to/new_directory}}`