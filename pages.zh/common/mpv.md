# mpv

> 基于 MPlayer 的音频/视频播放器。
> 另见：`mplayer`，`vlc`。
> 更多信息：<https://mpv.io>。

- 从 URL 或文件播放视频或音频：

`mpv {{url|path/to/file}}`

- 向后/向前跳跃 5 秒：

`LEFT <或> RIGHT`

- 向后/向前跳跃 1 分钟：

`DOWN <或> UP`

- 将播放速度降低或提高 10%：

`[ <或> ]`

- 截取当前帧的屏幕截图（默认保存为 `./mpv-shotNNNN.jpg`）：

`s`

- 以指定的速度播放文件（默认速度为 1）：

`mpv --speed {{0.01..100}} {{path/to/file}}`

- 使用 `mpv.conf` 文件中定义的配置文件播放文件：

`mpv --profile {{profile_name}} {{path/to/file}}`

- 显示网络摄像头或其他视频输入设备的输出：

`mpv {{/dev/video0}}`