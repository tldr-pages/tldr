# rkdeveloptool

> 用于闪存、转储和管理基于Rockchip的计算机设备的引导固件。
> 在通过USB连接设备之前，您需要将设备启动到Maskrom/Bootrom模式。
> 某些子命令可能需要以root权限运行。
> 更多信息：<https://github.com/rockchip-linux/rkdeveloptool>。

- [l] 列出所有连接的基于Rockchip的闪存[d]设备：

`rkdeveloptool ld`

- 通过强制设备[d]ownload并从指定文件安装[b]ootloader来初始化设备：

`rkdeveloptool db {{path/to/bootloader.bin}}`

- 使用新版本更新引导[l]oader软件：

`rkdeveloptool ul {{path/to/bootloader.bin}}`

- 将映像写入GPT格式的闪存分区，指定初始存储扇区（通常为`0x0`或`0`）：

`rkdeveloptool wl {{initial_sector}} {{path/to/image.img}}`

- 通过其用户友好的名称写入闪存分区：

`rkdeveloptool wlx {{partition_name}} {{path/to/image.img}}`

- [r]eset/reboot设备，从Maskrom/Bootrom模式退出以启动到选定的闪存分区：

`rkdeveloptool rd`