# cupsd

> CUPS打印服务器的服务器守护进程。
> 更多信息：<https://openprinting.github.io/cups/doc/man-cupsd.html>。

- 在后台启动 `cupsd`，即作为守护进程：

`cupsd`

- 在前台启动 `cupsd`：

`cupsd -f`

- 按需[l]aunch `cupsd`（通常由 `launchd` 或 `systemd` 使用）：

`cupsd -l`

- 使用指定的[`c`]`upsd.conf`配置文件启动 `cupsd`：

`cupsd -c {{path/to/cupsd.conf}}`

- 使用指定的 `cups-file`[`s`]`.conf`配置文件启动 `cupsd`：

`cupsd -s {{path/to/cups-files.conf}}`

- [t]est `cupsd.conf`配置文件的错误：

`cupsd -t -c {{path/to/cupsd.conf}}`

- [t]est `cups-file`[`s`]`.conf`配置文件的错误：

`cupsd -t -s {{path/to/cups-files.conf}}`

- 显示帮助：

`cupsd -h`