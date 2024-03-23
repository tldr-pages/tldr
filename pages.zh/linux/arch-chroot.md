# arch-chroot

> 辅助 Arch Linux 安装流程的更强 `chroot` 命令。
> 更多信息：<https://man.archlinux.org/man/arch-chroot.8>.

- 在新的根目录下开启一个交互外壳程序（默认是 Bash）：

`arch-chroot {{新根目录}}`

- 指定除当前用户外的其他用户来运行外壳程序：

`arch-chroot -u {{用户名}} {{新根目录}}`

- 在新的根目录下运行一个自定义命令（取代默认的 Bash）：

`arch-chroot {{新根目录}} {{命令}} {{命令参数}}`

- 指定除默认的 Bash 以外的外壳程序（以下例子需要现在目标系统中先安装 `zsh`）：

`arch-chroot {{新根目录}} {{zsh}}`
