# pueue add

> 将任务加入队列以执行。
> 更多信息：<https://github.com/Nukesor/pueue>.

- 将任何命令添加到默认队列：

`pueue add {{command}}`

- 在排队时向命令传递标志或参数列表：

`pueue add -- {{command --arg -f}}`

- 添加命令，但如果是队列中的第一个命令则不立即启动：

`pueue add --stashed -- {{rsync --archive --compress /local/directory /remote/directory}}`

- 将命令添加到组中并立即启动，参见 `pueue group` 管理组：

`pueue add --immediate --group "{{CPU_intensive}}" -- {{ffmpeg -i input.mp4 frame_%d.png}}`

- 在命令 9 和 12 成功完成后，将命令添加到组中并启动：

`pueue add --after {{9}} {{12}} --group "{{torrents}}" -- {{transmission-cli torrent_file.torrent}}`

- 延迟一段时间后，带有标签的命令，参见 `pueue enqueue` 了解有效的日期时间格式：

`pueue add --label "{{compressing large file}}" --delay "{{周三 22:30}}" -- "{{7z a compressed_file.7z large_file.xml}}"`