# ubus

> 与 OpenWrt 的 ubusd 服务器交互。
> 更多信息：<https://openwrt.org/docs/techref/ubus>。

- 列出可用的对象：

`ubus list`

- 以 JSON 格式获取系统信息：

`ubus call system board`

- 监听事件：

`ubus subscribe {{event_name}}`

- 显示帮助：

`ubus`