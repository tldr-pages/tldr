# blockdev

> 管理、查询和操作块设备。
> 更多信息：<https://manned.org/blockdev>.

- 打印所有设备的报告：

`sudo blockdev --report`

- 打印特定设备的报告：

`sudo blockdev --report {{/dev/sdXY}}`

- 获取设备的512字节扇区大小：

`sudo blockdev --getsz {{/dev/sdXY}}`

- 设置为只读：

`sudo blockdev --setro {{/dev/sdXY}}`

- 设置为读写：

`sudo blockdev --setrw {{/dev/sdXY}}`

- 刷新缓冲区：

`sudo blockdev --flushbufs {{/dev/sdXY}}`

- 获取物理块大小：

`sudo blockdev --getpbsz {{/dev/sdXY}}`

- 设置读取提前值为128个扇区：

`sudo blockdev --setra 128 {{/dev/sdXY}}`
