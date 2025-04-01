# cupsd

> CUPS 打印服务器的服务器守护进程。
> 更多信息：<https://openprinting.github.io/cups/doc/man-cupsd.html>.

- 在后台启动 `cupsd`，即作为守护进程启动：

`cupsd`

- 在前台启动 `cupsd`：

`cupsd -f`

- 按需启动 `cupsd`（通常由 `launchd` 或 `systemd` 使用）：

`cupsd -l`

- 使用指定的 `cupsd.conf` 配置文件启动 `cupsd`：

`cupsd -c {{path/to/cupsd.conf}}`

- 使用指定的 `cups-files.conf` 配置文件启动 `cupsd`：

`cupsd -s {{path/to/cups-files.conf}}`

- 检查 `cupsd.conf` 配置文件是否存在错误：

`cupsd -t -c {{path/to/cupsd.conf}}`

- 检查 `cups-files.conf` 配置文件是否存在错误：

`cupsd -t -s {{path/to/cups-files.conf}}`

- 显示帮助：

`cupsd -h`
