# hcitool

> 监控、配置连接和向蓝牙设备发送特殊命令。
> 更多信息：<https://manned.org/hcitool>.

- 扫描蓝牙设备：

`hcitool scan`

- 输出设备名称，返回其 MAC 地址：

`hcitool name {{bdaddr}}`

- 获取远程蓝牙设备的信息：

`hcitool info {{bdaddr}}`

- 检查与蓝牙设备的连接质量：

`hcitool lq {{bdaddr}}`

- 修改传输功率级别：

`hcitool tpl {{bdaddr}} {{0|1}}`

- 显示连接策略：

`hcitool lp`

- 请求与特定设备进行身份验证：

`hcitool auth {{bdaddr}}`

- 显示本地设备：

`hcitool dev`