# mkosi

> 构建现代、无遗留的 Linux 镜像。
> `systemd` 的一部分。
> 更多信息：<https://manned.org/mkosi>。

- 显示当前构建配置，以验证将要构建的内容：

`mkosi summary`

- 使用默认设置构建一个镜像（如果没有选择发行版，将使用主机系统的发行版）：

`mkosi build --distribution {{fedora|debian|ubuntu|arch|opensuse|...}}`

- 构建一个镜像并在 `systemd-nspawn` 容器中运行交互式 shell：

`mkosi shell`

- 使用 QEMU 引导一个镜像（仅支持磁盘镜像或提供内核的 CPIO 镜像）：

`mkosi qemu`

- 显示帮助：

`mkosi help`