# audacious

> 一个开源音频播放器，间接基于 XMMS。
> 参见：`audtool`, `clementine`, `mpc`, `ncmpcpp`。
> 更多信息：<https://audacious-media-player.org>。

- 启动图形界面：

`audacious`

- 启动新实例并播放音频：

`audacious --new-instance {{path/to/audio}}`

- 将特定目录中的音频文件添加到播放队列：

`audacious --enqueue {{path/to/directory}}`

- 开始或暂停播放：

`audacious --play-pause`

- 在播放列表中跳过（向前 [fwd] 或向后 [rew]）：

`audacious --{{fwd|rew}}`

- 停止播放：

`audacious --stop`

- 以命令行模式（无头模式）启动：

`audacious --headless`

- 播放结束后或没有任何播放内容时退出：

`audacious --quit-after-play`
