# modprobe

> 向 Linux 内核添加或移除模块。
> 参见：`kmod`，用于其他模块管理命令。
> 更多信息：<https://manned.org/modprobe>。

- 模拟加载模块到内核，但实际并不执行加载：

`sudo modprobe --dry-run {{module_name}}`

- 加载模块到内核：

`sudo modprobe {{module_name}}`

- 从内核中移除模块：

`sudo modprobe --remove {{module_name}}`

- 从内核中移除模块及其依赖项：

`sudo modprobe --remove-dependencies {{module_name}}`

- 显示内核模块的依赖项：

`sudo modprobe --show-depends {{module_name}}`
