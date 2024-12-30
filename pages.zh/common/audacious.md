# audacious

> 一个开源音频播放器。间接基于XMMS。
> 另见：`audtool`、`clementine`、`mpc`、`ncmpcpp`。
> 更多信息：<https://audacious-media-player.org>。

- 启动图形用户界面：

`audacious`

- 启动一个新实例并播放音频：

`audacious --new-instance {{path/to/audio}}`

- 将特定目录的音频文件加入播放列表：

`audacious --enqueue {{path/to/directory}}`

- 开始或暂停播放：

`audacious --play-pause`

- 在播放列表中向前 ([fwd]) 或向后 ([rew]) 跳转：

`audacious --{{fwd|rew}}`

- 停止播放：

`audacious --stop`

- 以CLI模式（无头模式）启动：

`audacious --headless`

- 播放停止后或没有内容可播放时立即退出：

`audacious --quit-after-play`