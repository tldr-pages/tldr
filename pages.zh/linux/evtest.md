# evtest

> 显示输入设备驱动的信息。
> 更多信息：<https://manned.org/evtest>.

- 列出所有检测到的输入设备：

`sudo evtest`

- 显示来自特定输入设备的事件：

`sudo evtest /dev/input/event{{number}}`

- 独占设备，防止其他客户端接收事件：

`sudo evtest --grab /dev/input/event{{number}}`

- 查询输入设备上特定按键或按钮的状态：

`sudo evtest --query /dev/input/event{{number}} {{event_type}} {{event_code}}`