# hyprctl

> 控制 Hyprland Wayland 合成器的部分组件。
> 更多信息：<https://wiki.hyprland.org/Configuring/Using-hyprctl>。

- 重新加载 Hyprland 配置：

`hyprctl reload`

- 返回活动窗口名称：

`hyprctl activewindow`

- 列出所有连接的输入设备：

`hyprctl devices`

- 列出所有输出及其相应属性：

`hyprctl workspaces`

- 调用调度器：

`hyprctl dispatch {{dispatcher}}`

- 动态设置配置关键字：

`hyprctl keyword {{keyword}} {{value}}`

- 显示版本：

`hyprctl version`