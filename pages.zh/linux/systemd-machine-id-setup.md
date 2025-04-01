# systemd-machine-id-setup

> 初始化安装时存储在 `/etc/machine-id` 中的机器 ID，可以使用预生成的或随机生成的 ID。
> 注意：执行这些命令时始终使用 `sudo`，因为它们需要提升的权限。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemd-machine-id-setup.html>.

- 打印生成的或已提交的机器 ID：

`systemd-machine-id-setup --print`

- 指定映像策略：

`systemd-machine-id-setup --image-policy={{your_policy}}`

- 以 JSON 格式显示输出：

`sudo systemd-machine-id-setup --json=pretty`

- 在磁盘映像上操作而不是目录树：

`systemd-machine-id-setup --image={{/path/to/image}}`
