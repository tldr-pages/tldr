# gh 屏幕保护程序

> GitHub CLI 的扩展，运行动画终端屏幕保护程序。
> 另见：`gh extension`。
> 更多信息：<https://github.com/vilmibm/gh-screensaver>。

- 运行随机屏幕保护程序：

`gh screensaver`

- 运行特定的屏幕保护程序：

`gh screensaver --saver {{fireworks|life|marquee|pipes|pollock|starfield}}`

- 运行带有特定文本和字体的“跑马灯”屏幕保护程序：

`gh screensaver --saver {{marquee}} -- --message="{{message}}" --font={{font_name}}`

- 运行带有特定密度和速度的“星空”屏幕保护程序：

`gh screensaver --saver {{starfield}} -- --density {{500}} --speed {{10}}`

- 列出可用的屏幕保护程序：

`gh screensaver --list`