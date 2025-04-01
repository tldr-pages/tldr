# vboxmanage-createvm

> 创建新的虚拟机。
> 更多信息：<https://www.virtualbox.org/manual/ch08.html#vboxmanage-createvm>.

- 使用默认设置创建新的虚拟机：

`VBoxManage createvm --name {{vm_name}}`

- 设置将存储虚拟机配置的基本文件夹：

`VBoxManage createvm --name {{vm_name}} --basefolder {{path/to/directory}}`

- 为导入的虚拟机设置客户操作系统类型（可选值为 `VBoxManage list ostypes` 中的一个）：

`VBoxManage createvm --name {{vm_name}} --ostype {{ostype}}`

- 在 VirtualBox 中注册创建的虚拟机：

`VBoxManage createvm --name {{vm_name}} --register`

- 将虚拟机设置到指定的组：

`VBoxManage createvm --name {{vm_name}} --group {{group1,group2,...}}`

- 设置虚拟机的全局唯一标识符（UUID）：

`VBoxManage createvm --name {{vm_name}} --uuid {{uuid}}`

- 设置用于加密的密码算法：

`VBoxManage createvm --name {{vm_name}} --cipher {{AES-128|AES-256}}`