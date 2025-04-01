# systemd-id128

> 生成并打印 sd-128 标识符。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemd-id128.html>.

- 生成一个新的随机标识符：

`systemd-id128 new`

- 打印当前机器的标识符：

`systemd-id128 machine-id`

- 打印当前启动的标识符：

`systemd-id128 boot-id`

- 打印当前服务调用的标识符（此功能在 systemd 服务中可用）：

`systemd-id128 invocation-id`

- 生成一个新的随机标识符并以 UUID 格式（五组数字，用破折号分隔）打印：

`systemd-id128 new --uuid`