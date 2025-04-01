# setsebool

> 设置 SELinux 布尔值。
> 相关命令：`semanage-boolean`, `getsebool`。
> 更多信息：<https://manned.org/setsebool>。

- 显示所有布尔值的当前设置：

`getsebool -a`

- 临时（重启后不保留）设置或取消设置布尔值：

`sudo setsebool {{httpd_can_network_connect}} {{1|true|on|0|false|off}}`

- 持久设置或取消设置布尔值：

`sudo setsebool -P {{container_use_devices}} {{1|true|on|0|false|off}}`

- 一次性持久设置或取消设置多个布尔值：

`sudo setsebool -P {{ftpd_use_fusefs=1 mount_anyfile=0 ...}}`

- 持久设置或取消设置布尔值（使用 `semanage-boolean` 的替代方法）：

`sudo semanage boolean {{[-m|--modify]}} {{-1|--on|-0|--off}} {{haproxy_connect_any}}`