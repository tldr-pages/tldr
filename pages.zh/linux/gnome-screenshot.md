# gnome-screenshot

> 捕获屏幕、窗口或用户定义区域，并将图像保存到文件。
> 更多信息：<https://manned.org/gnome-screenshot>。

- 截取屏幕截图并保存到默认位置，通常是 `~/Pictures`：

`gnome-screenshot`

- 截取屏幕截图并保存到指定的文件位置：

`gnome-screenshot --file {{path/to/file}}`

- 截取屏幕截图并保存到剪贴板：

`gnome-screenshot --clipboard`

- 在指定的秒数后截取屏幕截图：

`gnome-screenshot --delay {{5}}`

- 启动 GNOME 截图 GUI：

`gnome-screenshot --interactive`

- 截取当前窗口的屏幕截图并保存到指定的文件位置：

`gnome-screenshot --window --file {{path/to/file}}`

- 在指定的秒数后截取屏幕截图并保存到剪贴板：

`gnome-screenshot --delay {{10}} --clipboard`

- 显示版本：

`gnome-screenshot --version`