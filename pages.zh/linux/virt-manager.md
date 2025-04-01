# virt-manager

> 一个用于管理和监控 KVM 和 Xen 虚拟机及 LXC 容器的桌面用户界面。
> 更多信息：<https://manned.org/virt-manager.1>.

- 启动图形用户界面：

`virt-manager`

- 连接到虚拟机监控程序：

`virt-manager --connect {{hypervisor_uri}}`

- 启动时不将 virt-manager 进程分离到后台运行：

`virt-manager --no-fork`

- 输出调试信息：

`virt-manager --debug`

- 打开“新建虚拟机”向导：

`virt-manager --show-domain-creator`

- 打开特定虚拟机或容器的域详情窗口：

`virt-manager --show-domain-editor {{name|id|uuid}}`

- 打开特定虚拟机或容器的性能监控窗口：

`virt-manager --show-domain-performance {{name|id|uuid}}`

- 打开连接详情窗口：

`virt-manager --show-host-summary`
