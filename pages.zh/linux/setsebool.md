# setsebool

> 设置 SELinux 布尔值。
> 另见：`semanage-boolean`，`getsebool`。
> 更多信息：<https://manned.org/setsebool>。

- 显示 [所有] 布尔值的当前设置：

`getsebool -a`

- 临时设置或取消布尔值（在重启后不持久化）：

`sudo setsebool {{httpd_can_network_connect}} {{1|true|on|0|false|off}}`

- 持久性地设置或取消布尔值：

`sudo setsebool -P {{container_use_devices}} {{1|true|on|0|false|off}}`

- 一次性持久性地设置或取消多个布尔值：

`sudo setsebool -P {{ftpd_use_fusefs=1 mount_anyfile=0 ...}}`

- 持久性地设置或取消布尔值（使用 `semanage-boolean` 的替代方法）：

`sudo semanage boolean {{-m|--modify}} {{-1|--on|-0|--off}} {{haproxy_connect_any}}`