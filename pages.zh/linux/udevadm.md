# udevadm

> Linux `udev` 管理工具。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/udevadm>。

- 监控所有设备事件：

`sudo udevadm monitor`

- 打印内核发送的 `uevents`：

`sudo udevadm monitor --kernel`

- 打印经过 `udev` 处理后的设备事件：

`sudo udevadm monitor --udev`

- 列出设备 `/dev/sda` 的属性：

`sudo udevadm info --attribute-walk {{/dev/sda}}`

- 重新加载所有 `udev` 规则：

`sudo udevadm control --reload-rules`

- 触发所有 `udev` 规则运行：

`sudo udevadm trigger`

- 通过模拟加载 `/dev/sda` 测试事件：

`sudo udevadm test {{/dev/sda}}`