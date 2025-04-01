# wpctl

> 管理 WirePlumber，一个 PipeWire 的会话和策略管理器。
> 注意：可以使用特殊名称 `@DEFAULT_SINK@` 代替 `id` 来操作默认的音频输出设备。
> 更多信息：<https://pipewire.pages.freedesktop.org/wireplumber/>.

- 列出所有由 WirePlumber 管理的对象：

`wpctl status`

- 打印对象的所有属性：

`wpctl inspect {{id}}`

- 将对象设置为其组中的默认对象：

`wpctl set-default {{id}}`

- 获取音频输出设备的音量：

`wpctl get-volume {{id}}`

- 将音频输出设备的音量设置为 `n` 百分比：

`wpctl set-volume {{id}} {{n}}%`

- 将音频输出设备的音量增加/减少 `n` 百分比：

`wpctl set-volume {{id}} {{n}}%{{+|-}}`

- 静音/取消静音音频输出设备（1 表示静音，0 表示取消静音）：

`wpctl set-mute {{id}} {{1|0|toggle}}`