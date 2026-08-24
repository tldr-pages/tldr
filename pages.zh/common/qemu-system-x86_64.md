# qemu-system-x86_64

> 模拟 `x86_64` 架构。
> 更多信息：<https://www.qemu.org/docs/master/system/target-i386.html>。

- 从一个模拟 `x86_64` 架构的镜像启动：

`qemu-system-x86_64 -hda {{镜像名称.img}} -m {{4096}}`

- 从一个 Live ISO 镜像启动 QEMU 实例：

`qemu-system-x86_64 -hda {{镜像名称.img}} -m {{4096}} -cdrom {{操作系统镜像.iso}} -boot d`

- 从物理设备启动（例如：从 USB 启动以测试一个可启动介质）：

`qemu-system-x86_64 -hda {{/dev/存储设备}} -m {{4096}}`

- 不启动 VNC 服务器：

`qemu-system-x86_64 -hda {{镜像名称.img}} -m {{4096}} -nographic`

- 退出非图形界面的 QEMU：

`<Ctrl a><x>`

- 列出支持的机器类型：

`qemu-system-x86_64 {{[-M|-machine]}} help`
