# virsh-undefine

> 删除虚拟机。
> 更多信息：<https://manned.org/virsh>.

- 仅删除虚拟机配置文件：

`virsh undefine --domain {{vm_name}}`

- 删除配置文件和所有关联的存储卷：

`virsh undefine --domain {{vm_name}} --remove-all-storage`

- 使用目标名称或源名称（通过 `virsh domblklist` 命令获取）删除配置文件和指定的存储卷：

`virsh undefine --domain {{vm_name}} --storage {{sda,path/to/source}}`