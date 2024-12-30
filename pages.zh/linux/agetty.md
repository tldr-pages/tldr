# agetty

> 替代 `getty`：打开一个 `tty` 端口，提示输入登录名，并调用 `/bin/login` 命令。
> 它通常由 `init` 调用。
> 注意：波特率是指通过串行连接在终端和设备之间的数据传输速率。
> 更多信息：<https://manned.org/agetty>。

- 将 `stdin` 连接到一个端口（相对于 `/dev`），并可选地指定波特率（默认为 9600）：

`agetty {{tty}} {{115200}}`

- 假设 `stdin` 已经连接到一个 `tty`，并为登录设置超时：

`agetty {{-t|--timeout}} {{timeout_in_seconds}} -`

- 假设 `tty` 是 [8]-位，覆盖由 `init` 设置的 `TERM` 环境变量：

`agetty -8 - {{term_var}}`

- 跳过登录（不登录），以 root 身份调用另一个登录程序而不是 `/bin/login`：

`agetty {{-n|--skip-login}} {{-l|--login-program}} {{login_program}} {{tty}}`

- 在写入登录提示之前，不显示预登录（issue）文件（默认是 `/etc/issue`）：

`agetty {{-i|--noissue}} -`

- 更改根目录，并在 `utmp` 文件中写入一个特定的假主机：

`agetty {{-r|--chroot}} {{/path/to/root_directory}} {{-H|--host}} {{fake_host}} -`