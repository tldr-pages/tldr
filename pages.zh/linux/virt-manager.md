# virt-manager

> 一个用于管理 KVM 和 Xen 虚拟机及 LXC 容器的桌面用户界面。
> 更多信息：<https://manned.org/virt-manager.1>。

- 启动 GUI：

`virt-manager`

- 连接到超线程机：

`virt-manager --connect {{hypervisor_uri}}`

- 启动时不将 virt-manager 进程放入后台：

`virt-manager --no-fork`

- 打印调试输出：

`virt-manager --debug`

- 打开“新虚拟机”向导：

`virt-manager --show-domain-creator`

- 显示特定虚拟机/容器的域详细信息窗口：

`virt-manager --show-domain-editor {{name|id|uuid}}`

- 显示特定虚拟机/容器的域性能窗口：

`virt-manager --show-domain-performance {{name|id|uuid}}`

- 显示连接详细信息窗口：

`virt-manager --show-host-summary`