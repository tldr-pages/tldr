# dkms

> 一个允许动态构建内核模块的框架。
> 更多信息：<https://github.com/dell/dkms>.

- 列出当前已安装的模块：

`dkms status`

- 为当前运行的内核重新构建所有模块：

`dkms autoinstall`

- 为当前运行的内核安装 acpi_call 模块的 1.2.1 版本：

`dkms install -m {{acpi_call}} -v {{1.2.1}}`

- 从所有内核中移除 acpi_call 模块的 1.2.1 版本：

`dkms remove -m {{acpi_call}} -v {{1.2.1}} --all`