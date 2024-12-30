# mkosi

> 构建现代、无遗留的 Linux 镜像。
> 属于 `systemd`。
> 更多信息：<https://manned.org/mkosi>。

- 显示当前构建配置以验证将要构建的内容：

`mkosi summary`

- 使用默认设置构建镜像（如果未选择发行版，则使用主机系统的发行版）：

`mkosi build --distribution {{fedora|debian|ubuntu|arch|opensuse|...}}`

- 构建镜像并在该镜像的 systemd-nspawn 容器中运行交互式 shell：

`mkosi shell`

- 使用 QEMU 在虚拟机中启动镜像（仅支持磁盘镜像或在提供内核时的 CPIO 镜像）：

`mkosi qemu`

- 显示帮助信息：

`mkosi help`