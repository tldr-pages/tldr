# tlp-stat

> 生成 TLP 状态报告。
> 另见 `tlp`。
> 更多信息：<https://linrunner.de/tlp/usage/tlp-stat>。

- 生成包含配置和所有活动设置的状态报告：

`sudo tlp-stat`

- 显示各种设备的信息：

`sudo tlp-stat --{{battery|disk|processor|graphics|pcie|rfkill|usb}}`

- 显示支持详细信息的设备的详细信息：

`sudo tlp-stat {{[-v|--verbose]}} --{{battery|processor|pcie|usb}}`

- 显示配置：

`sudo tlp-stat {{[-c|--config]}}`

- 监控电源 `udev` 事件：

`sudo tlp-stat {{[-P|--pev]}}`

- 显示电源诊断信息：

`sudo tlp-stat --psup`

- 显示温度和风扇速度：

`sudo tlp-stat {{[-t|--temp]}}`

- 显示系统的一般信息：

`sudo tlp-stat {{[-s|--system]}}`