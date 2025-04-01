# vboxmanage-clonevm

> 创建现有虚拟机（VM）的克隆。
> 更多信息：<https://www.virtualbox.org/manual/ch08.html#vboxmanage-clonevm>。

- 克隆指定的虚拟机：

`VBoxManage clonevm {{vm_name}}`

- 为新虚拟机指定新名称：

`VBoxManage clonevm {{vm_name}} --name {{new_vm_name}}`

- 指定保存新虚拟机配置文件的文件夹：

`VBoxManage clonevm {{vm_name}} --basefolder {{path/to/directory}}`

- 在 VirtualBox 中注册克隆的虚拟机：

`VBoxManage clonevm {{vm_name}} --register`
