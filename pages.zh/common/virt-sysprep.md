# virt-sysprep

> 重置、取消配置或自定义虚拟机镜像。
> 更多信息：<https://manned.org/virt-sysprep>.

- 列出所有支持的操作（启用的操作用星号标记）：

`virt-sysprep --list-operations`

- 从虚拟机镜像中移除敏感系统数据：

`sudo virt-sysprep {{[-a|--add]}} {{path/to/image.qcow2}}`

- 指定虚拟机的名称，并运行所有启用的操作，但不实际应用更改：

`sudo virt-sysprep {{[-d|--domain]}} {{vm_name}} {{[-n|--dry-run]}}`

- 仅运行指定的操作：

`sudo virt-sysprep {{[-d|--domain]}} {{vm_name}} --operations {{operation1,operation2,...}}`

- 生成新的 `/etc/machine-id` 文件，并启用自定义以更改主机名来避免网络冲突：

`sudo virt-sysprep {{[-d|--domain]}} {{vm_name}} --enable {{customizations}} --hostname {{host_name}} --operation {{machine-id}}`

- 显示帮助：

`virt-sysprep {{[-he|--help]}}`
