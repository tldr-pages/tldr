# tart

> 在 Apple Silicon 上构建、运行和管理 macOS 和 Linux 虚拟机 (VM)。
> 更多信息：<https://github.com/cirruslabs/tart>。

- 拉取远程虚拟机镜像：

`tart pull {{acme.io/org/name:tag}}`

- 从本地或远程镜像源克隆虚拟机：

`tart clone {{source-vm}} {{vm-name}}`

- 从特定的 ipsw 文件创建新的 Mac 虚拟机：

`tart create --from-ipsw={{latest|path/to/file.ipsw}} {{vm-name}}`

- 运行现有虚拟机：

`tart run {{vm-name}}`

- 以特定挂载目录运行现有虚拟机：

`tart run --dir={{path/to/directory}}:{{/path/to/local_directory}} {{vm-name}}`

- 列出虚拟机：

`tart list`

- 获取正在运行的虚拟机的 IP 地址：

`tart ip {{vm-name}}`

- 更改虚拟机的显示分辨率：

`tart set {{vm-name}} --display {{640}}x{{400}}`