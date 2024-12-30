# pamixer

> 一个简单的PulseAudio命令行混音器。
> 更多信息：<https://github.com/cdemoulins/pamixer>。

- 列出所有音频输出和输入以及它们对应的ID：

`pamixer --list-sinks --list-sources`

- 将默认音频输出的音量设置为75%：

`pamixer --set-volume {{75}}`

- 切换默认以外的音频输出的静音状态：

`pamixer --toggle-mute --sink {{ID}}`

- 将默认音频输出的音量提高5%：

`pamixer --increase {{5}}`

- 将某个输入的音量降低5%：

`pamixer --decrease {{5}} --source {{ID}}`

- 使用允许提升选项将音量提高、降低或设置为超过100%：

`pamixer --set-volume {{105}} --allow-boost`

- 静音默认音频输出（使用`--unmute`来取消静音）：

`pamixer --mute`