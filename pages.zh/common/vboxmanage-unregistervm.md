# vboxmanage-unregistervm

> 注销虚拟机 (VM)。
> 更多信息：<https://www.virtualbox.org/manual/ch08.html#vboxmanage-unregistervm>。

- 注销现有的虚拟机：

`VBoxManage unregistervm {{uuid|vm_name}}`

- 删除硬盘镜像文件、所有保存状态文件、虚拟机日志和 XML 虚拟机文件：

`VBoxManage unregistervm {{uuid|vm_name}} --delete`

- 删除虚拟机的所有文件：

`VBoxManage unregistervm {{uuid|vm_name}} --delete-all`