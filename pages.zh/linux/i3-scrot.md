# i3-scrot

> 为 i3 窗口管理器提供截图工具 `scrot` 的封装脚本。
> 默认保存位置为 `~/Pictures`，可以在 `~/.config/i3-scrot.conf` 中更改。
> 更多信息：<https://gitlab.manjaro.org/packages/community/i3/i3-scrot>.

- 截取整个屏幕的截图并保存到默认目录：

`i3-scrot`

- 截取活动窗口的截图：

`i3-scrot --window`

- 截取特定矩形区域的截图：

`i3-scrot --select`

- 截取整个屏幕的截图并复制到剪贴板：

`i3-scrot --desk-to-clipboard`

- 截取活动窗口的截图并复制到剪贴板：

`i3-scrot --window-to-clipboard`

- 截取特定区域的截图并复制到剪贴板：

`i3-scrot --select-to-clipboard`

- 延迟 5 秒后截取活动窗口的截图：

`i3-scrot --window {{5}}`
