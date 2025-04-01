# limactl

> 用于管理 Linux 客户机虚拟机的工具，提供多种 VM 模板。
> 可用于在 macOS 上运行容器，也可用于 macOS 和 Linux 主机上的通用虚拟机用途。
> 更多信息：<https://github.com/lima-vm/lima>。

- 列出所有虚拟机：

`limactl list`

- 使用默认设置创建虚拟机，并可选地提供名称和/或模板（使用 `limactl create --list-templates` 查看可用模板）：

`limactl create --name {{vm_name}} template://{{debian|fedora|ubuntu|…}}`

- 启动虚拟机（这可能会在虚拟机内部安装一些依赖项并需要几分钟时间）：

`limactl start {{vm_name}}`

- 在虚拟机内打开远程 shell：

`limactl shell {{vm_name}}`

- 在虚拟机内运行命令：

`limactl shell {{vm_name}} {{command}}`

- 停止/关闭虚拟机：

`limactl stop {{vm_name}}`

- 删除虚拟机：

`limactl remove {{vm_name}}`