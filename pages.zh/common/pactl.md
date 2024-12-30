# pactl

> 控制正在运行的 PulseAudio 音频服务器。
> 更多信息: <https://manned.org/pactl>。

- 显示音频服务器的信息：

`pactl info`

- 列出所有音频输出（或其他类型 - 输出是音频输出，sink-input 是活动音频流）：

`pactl list {{sinks}} short`

- 将默认输出更改为 1（该数字可以通过 `list` 子命令获取）：

`pactl set-default-sink {{1}}`

- 将 sink-input 627 移动到 sink 1：

`pactl move-sink-input {{627}} {{1}}`

- 将 sink 1 的音量设置为 75%：

`pactl set-sink-volume {{1}} {{0.75}}`

- 切换默认输出的静音状态（使用特殊名称 `@DEFAULT_SINK@`）：

`pactl set-sink-mute {{@DEFAULT_SINK@}} toggle`