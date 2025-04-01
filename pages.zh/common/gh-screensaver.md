# gh screensaver

> GitHub CLI 的扩展，用于运行动画终端屏保。
> 参见：`gh extension`。
> 更多信息：<https://github.com/vilmibm/gh-screensaver>。

- 运行一个随机屏保：

`gh screensaver`

- 运行一个特定的屏保：

`gh screensaver --saver {{fireworks|life|marquee|pipes|pollock|starfield}}`

- 用特定文字和字体运行“marquee”屏保：

`gh screensaver --saver {{marquee}} -- --message="{{message}}" --font={{font_name}}`

- 用特定的密度和速度运行“starfield”屏保：

`gh screensaver --saver {{starfield}} -- --density {{500}} --speed {{10}}`

- 列出可用的屏保：

`gh screensaver --list`