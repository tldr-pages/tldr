# openttd

> 微软游戏“运输大亨豪华版”的开源克隆。
> 更多信息：<https://www.openttd.org>。

- 开始一个新游戏：

`openttd -g`

- 启动时加载保存的游戏：

`openttd -g {{path/to/file}}`

- 以指定的窗口分辨率启动：

`openttd -r {{1920x1080}}`

- 以自定义配置文件启动：

`openttd -c {{path/to/file}}`

- 以选择的视频、声音和音乐驱动程序启动：

`openttd -v {{video_driver}} -s {{sound_driver}} -m {{music_driver}}`

- 启动一个专用服务器，在后台运行：

`openttd -f -D {{host}}:{{port}}`

- 以密码加入服务器：

`openttd -n {{host}}:{{port}}#{{player_name}} -p {{password}}`