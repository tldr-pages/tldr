# openttd

> “Transport Tycoon Deluxe” 的开源克隆版。
> 更多信息：<https://www.openttd.org>。

- 开始新游戏：

`openttd -g`

- 启动时加载存档游戏：

`openttd -g {{path/to/file}}`

- 以指定的窗口分辨率启动：

`openttd -r {{1920x1080}}`

- 以自定义配置文件启动：

`openttd -c {{path/to/file}}`

- 选择视频、声音和音乐驱动程序启动：

`openttd -v {{video_driver}} -s {{sound_driver}} -m {{music_driver}}`

- 作为专用服务器在后台启动：

`openttd -f -D {{host}}:{{port}}`

- 使用密码加入服务器：

`openttd -n {{host}}:{{port}}#{{player_name}} -p {{password}}`
