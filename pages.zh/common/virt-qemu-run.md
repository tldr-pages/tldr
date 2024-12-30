# virt-qemu-run

> 一种实验性工具，用于独立于 `libvirtd` 运行 QEMU 客户虚拟机。
> 更多信息请访问：<https://libvirt.org/manpages/virt-qemu-run.html>。

- 运行一个 QEMU 虚拟机：

`virt-qemu-run {{path/to/guest.xml}}`

- 运行一个 QEMU 虚拟机，并将状态存储在特定目录中：

`virt-qemu-run --root={{path/to/directory}} {{path/to/guest.xml}}`

- 运行一个 QEMU 虚拟机，并显示关于启动的详细信息：

`virt-qemu-run --verbose {{path/to/guest.xml}}`

- 显示帮助信息：

`virt-qemu-run --help`