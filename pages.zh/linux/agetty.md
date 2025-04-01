# agetty

> 替代 `getty`：打开一个 `tty` 端口，提示输入登录名，并调用 `/bin/login` 命令。
> 通常由 `init` 调用。
> 注意：波特率是指终端和设备之间通过串行连接传输数据的速度。
> 更多信息：<https://manned.org/agetty>.

- 将 `stdin` 连接到端口（相对于 `/dev`），并可选地指定波特率（默认为 9600）：

`agetty {{tty}} {{115200}}`

- 假设 `stdin` 已经连接到 `tty`，并设置登录超时时间：

`agetty {{[-t|--timeout]}} {{超时秒数}} -`

- 假设 `tty` 是 8 位的，覆盖由 `init` 设置的 `TERM` 环境变量：

`agetty {{[-8|--8bits]}} - {{term_var}}`

- 跳过登录（不登录）并以 root 用户身份调用其他登录程序，而不是 `/bin/login`：

`agetty {{[-n|--skip-login]}} {{[-l|--login-program]}} {{登录程序}} {{tty}}`

- 不显示预先登录的文件（默认为 `/etc/issue`）：

`agetty {{[-i|--noissue]}} -`

- 更改根目录，并在 `utmp` 文件中写入特定的假主机名：

`agetty {{[-r|--chroot]}} {{/path/to/root_directory}} {{[-H|--host]}} {{假主机名}} -`