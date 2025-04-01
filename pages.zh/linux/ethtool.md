# ethtool

> 显示和修改网络接口控制器（NIC）的参数。
> 更多信息：<https://manned.org/ethtool>.

- 显示接口的当前设置：

`ethtool {{eth0}}`

- 显示接口的驱动信息：

`ethtool --driver {{eth0}}`

- 显示接口支持的所有功能：

`ethtool --show-features {{eth0}}`

- 显示接口的网络使用统计信息：

`ethtool --statistics {{eth0}}`

- 使接口的一个或多个LED闪烁10秒：

`ethtool --identify {{eth0}} {{10}}`

- 设置给定接口的链路速度、双工模式和自动协商参数：

`ethtool -s {{eth0}} speed {{10|100|1000}} duplex {{half|full}} autoneg {{on|off}}`