# dkms

> 一个允许动态构建内核模块的框架。
> 更多信息：<https://github.com/dell/dkms>。

- 列出当前已安装的模块：

`dkms status`

- 为当前正在运行的内核重建所有模块：

`dkms autoinstall`

- 为当前正在运行的内核安装版本 1.2.1 的 acpi_call 模块：

`dkms install -m {{acpi_call}} -v {{1.2.1}}`

- 从所有内核中移除版本 1.2.1 的 acpi_call 模块：

`dkms remove -m {{acpi_call}} -v {{1.2.1}} --all`