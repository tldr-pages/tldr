# vboxmanage-createvm

> 创建一个新的虚拟机。
> 更多信息：<https://www.virtualbox.org/manual/ch08.html#vboxmanage-createvm>。

- 使用默认设置创建一个新的虚拟机：

`VBoxManage createvm --name {{vm_name}}`

- 设置虚拟机配置将存储的基本文件夹：

`VBoxManage createvm --name {{vm_name}} --basefolder {{path/to/directory}}`

- 为导入的虚拟机设置客户操作系统类型（从 `VBoxManage list ostypes` 中选择之一）：

`VBoxManage createvm --name {{vm_name}} --ostype {{ostype}}`

- 在 VirtualBox 中注册创建的虚拟机：

`VBoxManage createvm --name {{vm_name}} --register`

- 将虚拟机设置为指定的组：

`VBoxManage createvm --name {{vm_name}} --group {{group1,group2,...}}`

- 设置虚拟机的通用唯一标识符（UUID）：

`VBoxManage createvm --name {{vm_name}} --uuid {{uuid}}`

- 设置要用于加密的密码：

`VBoxManage createvm --name {{vm_name}} --cipher {{AES-128|AES-256}}`