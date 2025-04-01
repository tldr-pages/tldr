# bless

> 设置卷的引导功能和启动磁盘选项。
> 更多信息：<https://keith.github.io/xcode-man-pages/bless.8.html>。

- 仅用于 macOS 或 Darwin 的卷进行 blessing，并按需创建 BootX 和 `boot.efi` 文件：

`bless --folder {{/Volumes/Mac OS X/System/Library/CoreServices}} --bootinfo --bootefi`

- 将包含 macOS 9 和 macOS 的卷设置为活动卷：

`bless --mount {{/Volumes/Mac OS}} --setBoot`

- 设置系统为网络启动，并广播查找可用服务器：

`bless --netboot --server {{bsdp://255.255.255.255}}`

- 收集有关当前选定卷（由固件确定）的信息，适合通过 Property Lists 解析的程序处理：

`bless --info --plist`
