# lxi

> 控制与 LXI 兼容的仪器，如示波器。
> 更多信息：<https://github.com/lxi-tools/lxi-tools>。

- 在可用网络上发现 LXI 设备：

`lxi discover`

- 截图，自动检测插件：

`lxi screenshot --address {{ip_address}}`

- 使用指定的插件截图：

`lxi screenshot --address {{ip_address}} --plugin {{rigol-1000z}}`

- 向仪器发送 SCPI 命令：

`lxi scpi --address {{ip_address}} "{{*IDN?}}"`

- 运行请求和响应性能的基准测试：

`lxi benchmark --address {{ip_address}}`
