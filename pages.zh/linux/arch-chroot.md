# arch-chroot

> 增强版的 `chroot` 命令，用于帮助 Arch Linux 的安装过程。
> 更多信息：<https://manned.org/arch-chroot.8>。

- 在新的根目录中启动一个交互式 shell（默认是 Bash）：

`arch-chroot {{path/to/new/root}}`

- 指定用户（与当前用户不同）以运行 shell：

`arch-chroot -u {{user}} {{path/to/new/root}}`

- 在新的根目录中运行自定义命令（而不是默认的 Bash）：

`arch-chroot {{path/to/new/root}} {{command}} {{command_arguments}}`

- 指定其他 shell，而不是默认的 Bash（在这种情况下，目标系统中应安装 `zsh` 包）：

`arch-chroot {{path/to/new/root}} {{zsh}}`