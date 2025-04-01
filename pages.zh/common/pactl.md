# pactl

> 控制正在运行的 PulseAudio 音频服务器。
> 更多信息：<https://manned.org/pactl>.

- 显示音频服务器的信息：

`pactl info`

- 列出所有音频输出设备（或其它类型 - 输出设备是指音频输出，输出流是指当前播放的音频流）：

`pactl list {{sinks}} short`

- 将默认输出设备更改为 1（数字可以通过 `list` 子命令获取）：

`pactl set-default-sink {{1}}`

- 将输出流 627 移动到输出设备 1：

`pactl move-sink-input {{627}} {{1}}`

- 将输出设备 1 的音量设置为 75%：

`pactl set-sink-volume {{1}} {{0.75}}`

- 切换默认输出设备的静音状态（使用特殊名称 `@DEFAULT_SINK@`）：

`pactl set-sink-mute {{@DEFAULT_SINK@}} toggle`
