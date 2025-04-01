# gnome-screenshot

> 捕获屏幕、窗口或用户定义的区域，并将图像保存到文件。
> 更多信息：<https://manned.org/gnome-screenshot>。

- 捕获屏幕快照并保存到默认位置，通常是 `~/Pictures`：

`gnome-screenshot`

- 捕获屏幕快照并保存到指定的文件位置：

`gnome-screenshot --file {{path/to/file}}`

- 捕获屏幕快照并保存到剪贴板：

`gnome-screenshot --clipboard`

- 在指定的秒数后捕获屏幕快照：

`gnome-screenshot --delay {{5}}`

- 启动 GNOME Screenshot 图形界面：

`gnome-screenshot --interactive`

- 捕获当前窗口的屏幕快照并保存到指定的文件位置：

`gnome-screenshot --window --file {{path/to/file}}`

- 在指定的秒数后捕获屏幕快照并保存到剪贴板：

`gnome-screenshot --delay {{10}} --clipboard`

- 显示版本信息：

`gnome-screenshot --version`