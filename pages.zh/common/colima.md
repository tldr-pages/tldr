# colima

> 适用于 macOS 和 Linux 的容器运行时，设置简单。
> 更多信息：<https://github.com/abiosoft/colima>。

- 在后台启动守护进程：

`colima start`

- 创建配置文件并使用它：

`colima start --edit`

- 启动并设置 containerd（安装 `nerdctl` 以通过 `nerdctl` 使用 containerd）：

`colima start --runtime containerd`

- 启动 Kubernetes（需要 `kubectl`）：

`colima start --kubernetes`

- 自定义 CPU 数量、内存和磁盘空间（以 GiB 为单位）：

`colima start --cpu {{number}} --memory {{memory}} --disk {{storage_space}}`

- 通过 Colima 使用 Docker（需要 Docker）：

`colima start`

- 列出容器及其信息和状态：

`colima list`

- 显示运行时状态：

`colima status`