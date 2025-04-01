# Xephyr

> 一个嵌套的 X 服务器，作为 X 应用程序运行。
> 更多信息：<https://manned.org/xserver-xephyr>.

- 创建一个显示 ID 为 ":2" 的黑色窗口：

`Xephyr -br -ac -noreset -screen {{800x600}} {{:2}}`

- 在新屏幕上启动一个 X 应用程序：

`DISPLAY=:2 {{command_name}}`