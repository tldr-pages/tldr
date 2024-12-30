# automount

> 读取 `/etc/auto_master` 文件，并在适当的挂载点上挂载 `autofs` 以触发按需挂载目录。基本上，这是一种手动启动系统自动挂载过程的方法。
> 注意：如果您没有必要的权限，您很可能需要使用 `sudo` 运行。
> 更多信息：<https://keith.github.io/xcode-man-pages/automount.8.html>。

- 运行 automount，提前刷新缓存（`-c`），并详细输出（`-v`）（最常用的用法）：

`automount -cv`

- 在 5 分钟（300 秒）不活动后自动卸载：

`automount -t 300`

- 卸载任何之前由 automount 挂载的内容和/或在 `/etc/auto_master` 中定义的内容：

`automount -u`