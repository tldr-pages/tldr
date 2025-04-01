# xbacklight

> 用于通过 RandR 扩展调整背光亮度的工具。
> 更多信息：<https://gitlab.freedesktop.org/xorg/app/xbacklight>。

- 获取当前屏幕亮度的百分比：

`xbacklight`

- 将屏幕亮度设置为 40%：

`xbacklight -set {{40}}`

- 将当前亮度增加 25%：

`xbacklight -inc {{25}}`

- 将当前亮度减少 75%：

`xbacklight -dec {{75}}`

- 在 60 秒内（以毫秒为单位给出值）使用 60 步骤将背光增加到 100%：

`xbacklight -set {{100}} -time {{60000}} -steps {{60}}`