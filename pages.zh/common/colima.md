# colima

> 为 macOS 和 Linux 提供容器运行环境，只需最少的设置。
> 更多信息：<https://github.com/abiosoft/colima>。

- 在后台启动守护进程：

`colima start`

- 创建配置文件并使用：

`colima start --edit`

- 启动并设置 containerd（安装 `nerdctl` 以通过 `nerdctl` 使用 containerd）：

`colima start --runtime containerd`

- 启用 Kubernetes（需要 `kubectl`）：

`colima start --kubernetes`

- 自定义 CPU 核心数、内存和磁盘空间（单位为 GiB）：

`colima start --cpu {{number}} --memory {{memory}} --disk {{storage_space}}`

- 通过 Colima 使用 Docker（需要 Docker）：

`colima start`

- 列出容器及其信息和状态：

`colima list`

- 显示运行状态：

`colima status`
