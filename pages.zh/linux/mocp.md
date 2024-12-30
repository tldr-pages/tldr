# mocp

> 音乐控制台 (MOC) 音频播放器。
> 更多信息：<https://manned.org/mocp>。

- 启动 MOC 终端用户界面：

`mocp`

- 在特定目录中启动 MOC 终端用户界面：

`mocp {{path/to/directory}}`

- 在后台启动 MOC 服务器，而不启动 MOC 终端用户界面：

`mocp --server`

- 在 MOC 在后台运行时将特定歌曲添加到播放队列：

`mocp --enqueue {{path/to/audio_file}}`

- 在 MOC 在后台运行时递归添加歌曲到播放队列：

`mocp --append {{path/to/directory}}`

- 在 MOC 在后台运行时清空播放队列：

`mocp --clear`

- 在 MOC 在后台运行时播放或停止当前排队的歌曲：

`mocp --{{play|stop}}`

- 在后台停止 MOC 服务器：

`mocp --exit`