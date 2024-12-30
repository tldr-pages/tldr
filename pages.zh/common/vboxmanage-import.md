# vboxmanage-import

> 导入之前导出的虚拟机（VM）。
> 更多信息：<https://www.virtualbox.org/manual/ch08.html#vboxmanage-import>。

- 从 OVF 或 OVA 文件导入虚拟机：

`VBoxManage import {{path/to/file.ovf}}`

- 设置导入虚拟机的名称：

`VBoxManage import {{path/to/file.ovf}} --name {{vm_name}}`

- 指定导入虚拟机的配置将存储的文件夹：

`VBoxManage import {{path/to/file.ovf}} --basefolder {{path/to/directory}}`

- 在 VirtualBox 中注册导入的虚拟机：

`VBoxManage import {{path/to/file.ovf}} --register`

- 执行干运行以检查导入，而不实际导入：

`VBoxManage import {{path/to/file.ovf}} --dry-run`

- 为导入的虚拟机设置客户操作系统类型（来自 `VBoxManage list ostypes` 的选项之一）：

`VBoxManage import {{path/to/file.ovf}} --ostype={{ostype}}`

- 为导入的虚拟机设置内存（以兆字节为单位）：

`VBoxManage import {{path/to/file.ovf}} --memory={{1}}`

- 为导入的虚拟机设置 CPU 数量：

`VBoxManage import {{path/to/file.ovf}} --cpus={{1}}`