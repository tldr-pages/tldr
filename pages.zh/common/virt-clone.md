# virt-clone

> 克隆 libvirt 虚拟机。
> 更多信息： <https://manned.org/virt-clone>.

- 克隆虚拟机并自动生成新的名称、存储路径和 MAC 地址：

`virt-clone --original {{vm_name}} --auto-clone`

- 克隆虚拟机并指定新的名称、存储路径和 MAC 地址：

`virt-clone --original {{vm_name}} --name {{new_vm_name}} --file {{path/to/new_storage}} --mac {{ff:ff:ff:ff:ff:ff|RANDOM}}`
