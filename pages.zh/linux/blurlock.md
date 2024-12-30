# blurlock

> 一个简单的包装器，围绕 i3 屏幕锁定器 `i3lock`，可以模糊屏幕。
> 参见：`i3lock`。
> 更多信息：<https://gitlab.manjaro.org/packages/community/i3/i3exit/-/blob/master/blurlock>。

- 将屏幕锁定到当前屏幕的模糊截图：

`blurlock`

- 锁定屏幕并禁用解锁指示器（移除按键反馈）：

`blurlock --no-unlock-indicator`

- 锁定屏幕并不隐藏鼠标指针：

`blurlock --pointer {{default}}`

- 锁定屏幕并显示失败的登录尝试次数：

`blurlock --show-failed-attempts`