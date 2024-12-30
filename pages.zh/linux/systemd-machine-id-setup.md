# systemd-machine-id-setup

> 在安装时使用预配置或随机生成的 ID 初始化存储在 `/etc/machine-id` 中的机器 ID。
> 注意：始终使用 `sudo` 执行这些命令，因为它们需要提升的权限。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemd-machine-id-setup.html>。

- 打印生成或提交的机器 ID：

`systemd-machine-id-setup --print`

- 指定镜像策略：

`systemd-machine-id-setup --image-policy={{your_policy}}`

- 将输出显示为 JSON 格式：

`sudo systemd-machine-id-setup --json=pretty`

- 在磁盘映像上操作，而不是目录树：

`systemd-machine-id-setup --image={{/path/to/image}}`