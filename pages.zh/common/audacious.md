# audacious

> 一个开源的音频播放器，间接基于 XMMS。
> 请参阅：`audtool`、`clementine`、`mpc`、`ncmpcpp`。
> 更多信息：<https://manned.org/audacious>.

- 启动图形用户界面：

`audacious`

- 启动一个新的实例并播放音频：

`audacious {{[-N|--new-instance]}} {{路径/到/音频}}`

- 将指定目录中的音频文件加入播放队列：

`audacious {{[-e|--enqueue]}} {{路径/到/目录}}`

- 开始或暂停播放：

`audacious {{[-t|--play-pause]}}`

- 在播放列表中向前（[fwd]）或向后（[rew]）跳转：

`audacious --{{fwd|rew}}`

- 停止播放：

`audacious {{[-s|--stop]}}`

- 以命令行模式（无界面）启动：

`audacious {{[-H|--headless]}}`

- 在播放结束或没有可播放内容时立即退出：

`audacious {{[-q|--quit-after-play]}}`
