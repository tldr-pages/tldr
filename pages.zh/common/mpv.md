# mpv

> 一个基于 MPlayer 的音频/视频播放器。
> 请参阅：`mplayer`, `vlc`。
> 更多信息：<https://mpv.io/manual/stable/>.

- 从 URL 或文件播放视频或音频：

`mpv {{url|路径/到/文件}}`

- 向后/向前跳跃 5 秒：

`{{<ArrowLeft>|<ArrowRight>}}`

- 向后/向前跳跃 1 分钟：

`{{<ArrowDown>|<ArrowUp>}}`

- 减少/增加 10% 播放速度：

`{{<[>|<]>}}`

- 对当前帧截图（默认保存到 `./mpv-shotNNNN.jpg`）：

`<s>`

- 以指定速度播放文件（0.01 到 100, 默认是 1）：

`mpv --speed {{0.01..100}} {{路径/到/文件}}`

- 用 `mpv.conf` 中指定的一个用户配制播放文件：

`mpv --profile {{配置文件名称}} {{路径/到/文件}}`

- 显示来自网络摄像头或其他视频输入设备的输出：

`mpv {{/dev/video0}}`
