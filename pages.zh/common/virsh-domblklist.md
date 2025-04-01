# virsh-domblklist

> 列出与虚拟机关联的块设备的信息。
> 参见：`virsh`。
> 更多信息：<https://manned.org/virsh>。

- 列出块设备的目标名称和源路径：

`virsh domblklist --domain {{vm_name}}`

- 列出磁盘类型和设备值，以及目标名称和源路径：

`virsh domblklist --domain {{vm_name}} --details`
