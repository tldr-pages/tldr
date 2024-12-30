# wpctl

> 管理 WirePlumber，这是一个用于 PipeWire 的会话和策略管理器。
> 注意：您可以使用特殊名称 `@DEFAULT_SINK@` 来代替 `id` 以操作默认输出设备。
> 更多信息：<https://pipewire.pages.freedesktop.org/wireplumber/>.

- 列出所有由 WirePlumber 管理的对象：

`wpctl status`

- 打印对象的所有属性：

`wpctl inspect {{id}}`

- 将对象设置为其组中的默认项：

`wpctl set-default {{id}}`

- 获取输出设备的音量：

`wpctl get-volume {{id}}`

- 将输出设备的音量设置为 `n` 百分比：

`wpctl set-volume {{id}} {{n}}%`

- 将输出设备的音量增加/减少 `n` 百分比：

`wpctl set-volume {{id}} {{n}}%{{+|-}}`

- 静音/取消静音输出设备（1 为静音，0 为取消静音）：

`wpctl set-mute {{id}} {{1|0|toggle}}`