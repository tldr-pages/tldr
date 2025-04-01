# systemd-detect-virt

> 检测是否在虚拟化环境中执行。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemd-detect-virt.html>.

- 列出可检测的虚拟化技术：

`systemd-detect-virt --list`

- 检测虚拟化，如果在虚拟机或容器中运行则输出结果并返回状态码0，否则返回非零状态码：

`systemd-detect-virt`

- 静默检查，不输出任何内容：

`systemd-detect-virt --quiet`

- 仅检测容器虚拟化：

`systemd-detect-virt --container`

- 仅检测硬件虚拟化：

`systemd-detect-virt --vm`