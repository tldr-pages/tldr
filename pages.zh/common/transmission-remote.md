# transmission-remote

> 用于远程控制 `transmission-daemon` 和 `transmission` 的工具。
> 更多信息：<https://transmissionbt.com>。

- 向 Transmission 添加一个种子文件或磁力链接，并下载到指定的目录：

`transmission-remote {{hostname}} -a {{torrent|url}} -w {{/path/to/download_directory}}`

- 更改默认下载目录：

`transmission-remote {{hostname}} -w {{/path/to/download_directory}}`

- 列出所有种子：

`transmission-remote {{hostname}} --list`

- 启动种子 1 和 2，停止种子 3：

`transmission-remote {{hostname}} -t "{{1,2}}" --start -t {{3}} --stop`

- 删除种子 1 和 2，并删除种子 2 的本地数据：

`transmission-remote {{hostname}} -t {{1}} --remove -t {{2}} --remove-and-delete`

- 停止所有种子：

`transmission-remote {{hostname}} -t {{all}} --stop`

- 将种子 1-10 和 15-20 移动到新目录（如果目录不存在将被创建）：

`transmission-remote {{hostname}} -t "{{1-10,15-20}}" --move {{/path/to/new_directory}}`