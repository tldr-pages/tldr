# quickget

> 下载并准备构建 Quickemu 虚拟机的材料。
> 注意：参数“edition”始终是可选的。
> 另见：`quickemu`。
> 更多信息：<https://github.com/quickemu-project/quickemu>。

- 显示所有支持的来宾操作系统、版本和变体的列表：

`quickget list`

- 下载并创建用于构建 Quickemu 虚拟机的操作系统的虚拟机配置：

`quickget {{os}} {{release}} {{edition}}`

- 下载带有 Windows VirtIO 驱动程序的 Windows 11 虚拟机配置：

`quickget windows 11`

- 下载 macOS 恢复映像并创建虚拟机配置：

`quickget macos {{mojave|catalina|big-sur|monterey|ventura|sonoma}}`

- 显示操作系统的 ISO URL：

`quickget --url fedora {{release}} {{edition}}`

- 测试操作系统的 ISO 文件是否可用：

`quickget --check nixos {{release}} {{edition}}`

- 下载映像而不构建任何虚拟机配置：

`quickget --download {{os}} {{release}} {{edition}}`

- 为操作系统映像创建虚拟机配置：

`quickget --create-config {{os}} {{path/to/iso}}`