# pamixer

> 简单的命令行音量控制器，适用于 PulseAudio。
> 更多信息： <https://github.com/cdemoulins/pamixer>.

- 列出所有音频输出和输入设备及其对应的 ID：

`pamixer --list-sinks --list-sources`

- 将默认音频输出设备的音量设置为 75%：

`pamixer --set-volume {{75}}`

- 切换非默认音频输出设备的静音状态：

`pamixer --toggle-mute --sink {{ID}}`

- 将默认音频输出设备的音量提高 5%：

`pamixer --increase {{5}}`

- 将音频输入设备的音量降低 5%：

`pamixer --decrease {{5}} --source {{ID}}`

- 使用允许增益选项将音量提高、降低或设置为 100% 以上：

`pamixer --set-volume {{105}} --allow-boost`

- 静音默认音频输出设备（使用 `--unmute` 选项取消静音）：

`pamixer --mute`
