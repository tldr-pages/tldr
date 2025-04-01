# hdparm

> 获取和设置 SATA 和 IDE 硬盘参数。
> 更多信息：<https://manned.org/hdparm>.

- 请求指定设备的识别信息：

`sudo hdparm -I {{/dev/device}}`

- 获取高级电源管理级别：

`sudo hdparm -B {{/dev/device}}`

- 设置高级电源管理值（1-127 允许停转，128-254 不允许）：

`sudo hdparm -B {{1}} {{/dev/device}}`

- 显示设备当前的电源模式状态：

`sudo hdparm -C {{/dev/device}}`

- 强制硬盘立即进入待机模式（通常会使硬盘停转）：

`sudo hdparm -y {{/dev/device}}`

- 将硬盘置于低功耗（空闲）模式，并设置其待机超时时间：

`sudo hdparm -S {{standby_timeout}} {{device}}`

- 测试特定设备的读取速度：

`sudo hdparm -tT {{device}}`