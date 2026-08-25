# modprobe

> 从 Linux 内核添加或移除模块。
> 另请参阅：`kmod`。
> 更多信息：<https://manned.org/modprobe>。

- 假装将模块加载到内核中，但实际上不这样做：

`modprobe {{[-n|--dry-run]}} {{模块名}}`

- 加载模块到内核：

`sudo modprobe {{模块名}}`

- 从内核移除模块：

`sudo modprobe {{[-r|--remove]}} {{模块名}}`

- 从内核移除模块及所有依赖它的模块：

`sudo modprobe {{[-r|--remove]}} --remove-holders {{模块名}}`

- 显示内核模块的依赖：

`sudo modprobe {{[-D|--show-depends]}} {{模块名}}`
