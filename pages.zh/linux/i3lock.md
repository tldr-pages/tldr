# i3lock

> 为 i3 窗口管理器设计的简单屏幕锁定工具。
> 更多信息：<https://i3wm.org/i3lock>。

- 锁定屏幕并显示白色背景：

`i3lock`

- 锁定屏幕并使用简单颜色背景（格式为 rrggbb）：

`i3lock --color {{0000ff}}`

- 锁定屏幕并使用 PNG 图片作为背景：

`i3lock --image {{path/to/file.png}}`

- 锁定屏幕并禁用解锁指示器（移除按键反馈）：

`i3lock --no-unlock-indicator`

- 锁定屏幕并显示鼠标指针：

`i3lock --pointer {{default}}`

- 锁定屏幕并使用 PNG 图片作为平铺背景：

`i3lock --image {{path/to/file.png}} --tiling`

- 锁定屏幕并显示失败的登录尝试次数：

`i3lock --show-failed-attempts`
