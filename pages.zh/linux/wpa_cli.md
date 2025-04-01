# wpa_cli

> 添加和配置无线网络接口。
> 更多信息：<https://manned.org/wpa_cli>.

- 扫描可用网络：

`wpa_cli scan`

- 显示扫描结果：

`wpa_cli scan_results`

- 添加网络：

`wpa_cli add_network {{number}}`

- 设置网络的 SSID：

`wpa_cli set_network {{number}} ssid "{{SSID}}"`

- 启用网络：

`wpa_cli enable_network {{number}}`

- 保存配置：

`wpa_cli save_config`
