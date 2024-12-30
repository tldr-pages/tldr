# tlp-stat

> 生成 TLP 状态报告。
> 另见 `tlp`。
> 更多信息：<https://linrunner.de/tlp/usage/tlp-stat>。

- 生成包含配置和所有活动设置的状态报告：

`sudo tlp-stat`

- 显示有关各种设备的信息：

`sudo tlp-stat --{{battery|disk|processor|graphics|pcie|rfkill|usb}}`

- 显示支持详细信息的设备的详细信息：

`sudo tlp-stat --verbose --{{battery|processor|pcie|usb}}`

- 显示配置：

`sudo tlp-stat {{-c|--config}}`

- 监视 [p]ower 供应 `udev` [ev]ents：

`sudo tlp-stat {{-P|--pev}}`

- 显示 [p]ower [sup]ply 诊断信息：

`sudo tlp-stat --psup`

- 显示 [temp]eratures 和风扇速度：

`sudo tlp-stat {{-t|--temp}}`

- 显示一般系统信息：

`sudo tlp-stat {{-s|--system}}`