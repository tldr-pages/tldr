# swaylock

> 用于 Wayland 合成器的屏幕锁定工具。
> 更多信息：<https://manned.org/swaylock>。

- 锁定屏幕，显示白色背景：

`swaylock`

- 用简单的颜色背景锁定屏幕（rrggbb 格式）：

`swaylock --color {{0000ff}}`

- 锁定屏幕，使用 PNG 背景：

`swaylock --image {{path/to/file.png}}`

- 锁定屏幕并禁用解锁指示器（移除按键反馈）：

`swaylock --no-unlock-indicator`

- 锁定屏幕并不隐藏鼠标指针：

`swaylock --pointer {{default}}`

- 锁定屏幕，使用 PNG 背景在所有监视器上平铺：

`swaylock --image {{path/to/file.png}} --tiling`

- 锁定屏幕并显示失败的登录尝试次数：

`swaylock --show-failed-attempts`

- 从文件加载配置：

`swaylock --config {{path/to/config}}`