# getsebool

> 获取 SELinux 布尔值。
> 另见：`semanage-boolean`，`setsebool`。
> 更多信息：<https://manned.org/getsebool>。

- 显示布尔值的当前设置：

`getsebool {{httpd_can_connect_ftp}}`

- 显示所有布尔值的当前设置：

`getsebool -a`

- 显示所有布尔值的当前设置及其解释：

`sudo semanage boolean {{-l|--list}}`