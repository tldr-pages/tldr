# virt-sysprep

> 重置、取消配置或自定义虚拟机映像。
> 更多信息：<https://manned.org/virt-sysprep>。

- 列出所有支持的操作（启用的操作用星号表示）：

`virt-sysprep --list-operations`

- 运行所有启用的操作，但实际上不应用更改：

`virt-sysprep --domain {{vm_name}} --dry-run`

- 仅运行指定的操作：

`virt-sysprep --domain {{vm_name}} --operations {{operation1,operation2,...}}`

- 生成新的 `/etc/machine-id` 文件，并启用自定义以便更改主机名以避免网络冲突：

`virt-sysprep --domain {{vm_name}} --enable {{customizations}} --hostname {{host_name}} --operation {{machine-id}}`