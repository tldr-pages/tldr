# i3-scrot

> i3窗口管理器的截图工具`scrot`的包装脚本。
> 默认保存位置是`~/Pictures`，可以在`~/.config/i3-scrot.conf`中更改。
> 更多信息：<https://gitlab.manjaro.org/packages/community/i3/i3-scrot>。

- 捕获整个屏幕的截图并保存到默认目录：

`i3-scrot`

- 捕获活动窗口的截图：

`i3-scrot --window`

- 捕获特定矩形区域的截图：

`i3-scrot --select`

- 捕获整个屏幕的截图并复制到剪贴板：

`i3-scrot --desk-to-clipboard`

- 捕获活动窗口的截图并复制到剪贴板：

`i3-scrot --window-to-clipboard`

- 捕获特定区域的截图并复制到剪贴板：

`i3-scrot --select-to-clipboard`

- 在5秒延迟后捕获活动窗口的截图：

`i3-scrot --window {{5}}`