# bless

> 设置卷启动能力和启动磁盘选项。
> 更多信息: <https://keith.github.io/xcode-man-pages/bless.8.html>。

- 仅对 Mac OS X 或 Darwin 进行 bless，并根据需要创建 BootX 和 `boot.efi` 文件：

`bless --folder {{/Volumes/Mac OS X/System/Library/CoreServices}} --bootinfo --bootefi`

- 将包含 Mac OS 9 和 Mac OS X 的卷设置为活动卷：

`bless --mount {{/Volumes/Mac OS}} --setBoot`

- 设置系统为 NetBoot 并广播可用服务器：

`bless --netboot --server {{bsdp://255.255.255.255}}`

- 收集有关当前选定卷的信息（由固件确定），适合传递给能够解析属性列表的程序：

`bless --info --plist`