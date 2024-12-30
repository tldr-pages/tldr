# i3lock

> 为i3窗口管理器构建的简单屏幕锁定器。 
> 更多信息：<https://i3wm.org/i3lock>。

- 锁定屏幕，显示白色背景：

`i3lock`

- 锁定屏幕，使用简单颜色背景（rrggbb格式）：

`i3lock --color {{0000ff}}`

- 锁定屏幕，使用PNG背景：

`i3lock --image {{path/to/file.png}}`

- 锁定屏幕并禁用解锁指示器（移除按键反馈）：

`i3lock --no-unlock-indicator`

- 锁定屏幕并不隐藏鼠标指针：

`i3lock --pointer {{default}}`

- 锁定屏幕，使用PNG背景，在所有显示器上平铺：

`i3lock --image {{path/to/file.png}} --tiling`

- 锁定屏幕并显示失败登录尝试次数：

`i3lock --show-failed-attempts`