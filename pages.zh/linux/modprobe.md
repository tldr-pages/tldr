# modprobe

> 从Linux内核添加或删除模块。
> 更多信息：<https://manned.org/modprobe>。

- 假装将模块加载到内核中，但实际上不执行：

`sudo modprobe --dry-run {{module_name}}`

- 将模块加载到内核中：

`sudo modprobe {{module_name}}`

- 从内核中删除模块：

`sudo modprobe --remove {{module_name}}`

- 从内核中删除模块及其依赖的模块：

`sudo modprobe --remove-dependencies {{module_name}}`

- 显示内核模块的依赖关系：

`sudo modprobe --show-depends {{module_name}}`