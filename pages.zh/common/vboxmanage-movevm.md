# vboxmanage movevm

> 将虚拟机 (VM) 移动到主机系统上的新位置。
> 更多信息：<https://www.virtualbox.org/manual/ch08.html#vboxmanage-movevm>。

- 将指定的虚拟机移动到当前位置：

`VBoxManage movevm {{vm_name}}`

- 指定虚拟机的新位置（完整或相对路径）：

`VBoxManage movevm {{vm_name}} --folder {{path/to/new_location}}`