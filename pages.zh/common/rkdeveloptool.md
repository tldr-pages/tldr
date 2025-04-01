# rkdeveloptool

> 用于基于 Rockchip 的计算机设备的固件刷写、备份和管理。
> 在通过 USB 连接设备之前，需要将其切换到 Maskrom/Bootrom 模式。
> 某些子命令可能需要以 root 权限运行。
> 更多信息：<https://github.com/rockchip-linux/rkdeveloptool>.

- [l]列出所有连接的基于 Rockchip 的闪存 [d]设备：

`rkdeveloptool ld`

- 通过强制设备从指定文件 [d]下载并安装 [b]引导加载程序来初始化设备：

`rkdeveloptool db {{path/to/bootloader.bin}}`

- 使用新引导加载程序更新引导[l]加载程序软件：

`rkdeveloptool ul {{path/to/bootloader.bin}}`

- 将映像写入 GPT 格式的闪存分区，指定初始存储扇区（通常为 `0x0` 或 `0`）：

`rkdeveloptool wl {{initial_sector}} {{path/to/image.img}}`

- 通过分区的用户友好名称写入闪存分区：

`rkdeveloptool wlx {{partition_name}} {{path/to/image.img}}`

- [r]重置/重启 [d]设备，从 Maskrom/Bootrom 模式退出并引导到选定的闪存分区：

`rkdeveloptool rd`