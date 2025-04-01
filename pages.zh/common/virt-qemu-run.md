# virt-qemu-run

> 实验性工具，用于独立于 `libvirtd` 运行 QEMU 客户机虚拟机。
> 更多信息：<https://libvirt.org/manpages/virt-qemu-run.html>.

- 运行 QEMU 虚拟机：

`virt-qemu-run {{path/to/guest.xml}}`

- 运行 QEMU 虚拟机，并将状态存储在特定目录中：

`virt-qemu-run --root={{path/to/directory}} {{path/to/guest.xml}}`

- 运行 QEMU 虚拟机并显示启动的详细信息：

`virt-qemu-run --verbose {{path/to/guest.xml}}`

- 显示帮助信息：

`virt-qemu-run --help`