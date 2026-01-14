# automount

> 读取 `/etc/auto_master` 文件，并在适当的挂载点上挂载 `autofs`，以触发目录的按需挂载。本质上，这是一种手动启动系统自动挂载过程的方式。
> 注意：如果没有必要权限，很可能需要使用 `sudo` 运行。
> 更多信息：<https://keith.github.io/xcode-man-pages/automount.8.html>。

- 运行 automount，在此之前先清空缓存（`-c`），并显示详细信息（`-v`）（最常用的方式）：

`automount -cv`

- 在 5 分钟（300 秒）不活动后自动卸载：

`automount -t 300`

- 卸载所有先前由 automount 挂载的文件系统和/或在 `/etc/auto_master` 中定义的内容：

`automount -u`
