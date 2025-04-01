# tart

> 构建、运行和管理 Apple Silicon 上的 macOS 和 Linux 虚拟机 (VM)。
> 更多信息：<https://github.com/cirruslabs/tart>。

- 拉取远程 VM 镜像：

`tart pull {{acme.io/org/name:tag}}`

- 从本地或远程镜像源克隆 VM：

`tart clone {{source-vm}} {{vm-name}}`

- 从特定的 ipsw 文件创建新的 Mac VM：

`tart create --from-ipsw={{latest|path/to/file.ipsw}} {{vm-name}}`

- 运行现有的 VM：

`tart run {{vm-name}}`

- 运行现有的 VM 并挂载特定目录：

`tart run --dir={{path/to/directory}}:{{/path/to/local_directory}} {{vm-name}}`

- 列出 VM：

`tart list`

- 获取正在运行的 VM 的 IP 地址：

`tart ip {{vm-name}}`

- 更改 VM 的显示分辨率：

`tart set {{vm-name}} --display {{640}}x{{400}}`
