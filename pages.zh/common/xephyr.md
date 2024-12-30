# Xephyr

> 一个作为X应用程序运行的嵌套X服务器。
> 更多信息：<https://manned.org/xserver-xephyr>。

- 创建一个显示ID为 ":2" 的黑色窗口：

`Xephyr -br -ac -noreset -screen {{800x600}} {{:2}}`

- 在新屏幕上启动一个X应用程序：

`DISPLAY=:2 {{command_name}}`