# mocp

> Music on Console (MOC) 音频播放器。
> 更多信息：<https://manned.org/mocp>。

- 启动 MOC 终端用户界面：

`mocp`

- 在特定目录中启动 MOC 终端用户界面：

`mocp {{path/to/directory}}`

- 在后台启动 MOC 服务器，不启动 MOC 终端用户界面：

`mocp --server`

- 在后台将特定歌曲添加到播放队列：

`mocp --enqueue {{path/to/audio_file}}`

- 在后台递归添加歌曲到播放队列：

`mocp --append {{path/to/directory}}`

- 在后台清空播放队列：

`mocp --clear`

- 在后台播放或停止当前排队的歌曲：

`mocp --{{play|stop}}`

- 停止后台运行的 MOC 服务器：

`mocp --exit`