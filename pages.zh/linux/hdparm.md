# hdparm

> 获取和设置SATA及IDE硬盘参数。
> 更多信息：<https://manned.org/hdparm>。

- 请求给定设备的识别信息：

`sudo hdparm -I {{/dev/device}}`

- 获取高级电源管理级别：

`sudo hdparm -B {{/dev/device}}`

- 设置高级电源管理值（值1-127允许转动停止，值128-254不允许）：

`sudo hdparm -B {{1}} {{/dev/device}}`

- 显示设备的当前电源模式状态：

`sudo hdparm -C {{/dev/device}}`

- 强制驱动器立即进入待机模式（通常会导致驱动器停止旋转）：

`sudo hdparm -y {{/dev/device}}`

- 将驱动器置于空闲（低功耗）模式，并设置其待机超时：

`sudo hdparm -S {{standby_timeout}} {{device}}`

- 测试特定设备的读取速度：

`sudo hdparm -tT {{device}}`