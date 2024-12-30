# dmesg

> 将内核消息写入 `stdout`。
> 更多信息：<https://keith.github.io/xcode-man-pages/dmesg.8.html>。

- 显示内核消息：

`dmesg`

- 显示此系统上可用的物理内存量：

`dmesg | grep -i memory`

- 一次显示一页内核消息：

`dmesg | less`