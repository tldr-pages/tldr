# systemd-detect-virt

> 检测在虚拟化环境中的执行。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemd-detect-virt.html>。

- 列出可检测的虚拟化技术：

`systemd-detect-virt --list`

- 检测虚拟化，打印结果并在虚拟机或容器中运行时返回零状态码，其他情况下返回非零代码：

`systemd-detect-virt`

- 静默检查，不打印任何内容：

`systemd-detect-virt --quiet`

- 仅检测容器虚拟化：

`systemd-detect-virt --container`

- 仅检测硬件虚拟化：

`systemd-detect-virt --vm`