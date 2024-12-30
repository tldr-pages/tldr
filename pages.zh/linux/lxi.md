# lxi

> 控制兼容LXI的仪器，例如示波器。
> 更多信息：<https://github.com/lxi-tools/lxi-tools>。

- 在可用网络上发现LXI设备：

`lxi discover`

- 捕获屏幕截图，自动检测插件：

`lxi screenshot --address {{ip_address}}`

- 使用指定插件捕获屏幕截图：

`lxi screenshot --address {{ip_address}} --plugin {{rigol-1000z}}`

- 向仪器发送SCPI命令：

`lxi scpi --address {{ip_address}} "{{*IDN?}}"`

- 运行请求和响应性能基准测试：

`lxi benchmark --address {{ip_address}}`