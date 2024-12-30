# limactl

> 一款用于管理Linux虚拟机的虚拟机管理器，提供多种虚拟机模板。
> 可用于在macOS上运行容器，也可用于在macOS和Linux主机上的通用虚拟机用例。
> 更多信息：<https://github.com/lima-vm/lima>。

- 列出虚拟机：

`limactl list`

- 使用默认设置创建虚拟机，并可选择提供名称和/或模板（查看 `limactl create --list-templates` 以获取可用模板）：

`limactl create --name {{vm_name}} template://{{debian|fedora|ubuntu|…}}`

- 启动虚拟机（这可能会安装一些依赖项，可能需要几分钟）：

`limactl start {{vm_name}}`

- 在虚拟机内打开远程 shell：

`limactl shell {{vm_name}}`

- 在虚拟机内运行命令：

`limactl shell {{vm_name}} {{command}}`

- 停止/关闭虚拟机：

`limactl stop {{vm_name}}`

- 删除虚拟机：

`limactl remove {{vm_name}}`