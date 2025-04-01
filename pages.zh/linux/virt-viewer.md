# virt-viewer

> 虚拟机（VM）的最小图形界面。
> 注意：'domain' 指的是现有虚拟机的名称、UUID 或 ID（参见：tldr virsh）。
> 更多信息：<https://manned.org/virt-viewer>。

- 启动 `virt-viewer` 并提示选择正在运行的虚拟机：

`virt-viewer`

- 通过 ID、UUID 或名称启动特定虚拟机的 `virt-viewer`：

`virt-viewer "{{domain}}"`

- 等待虚拟机启动并在其关闭和重启后自动重新连接：

`virt-viewer --reconnect --wait "{{domain}}"`

- 通过 TLS 连接到特定远程虚拟机：

`virt-viewer --connect "xen//{{url}}" "{{domain}}"`

- 通过 SSH 连接到特定远程虚拟机：

`virt-viewer --connect "qemu+ssh//{{username}}@{{url}}/system" "{{domain}}"`