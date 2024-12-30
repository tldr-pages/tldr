# getent

> 从名称服务开关库获取条目。
> 更多信息：<https://manned.org/getent>。

- 获取所有组的列表：

`getent group`

- 查看组的成员：

`getent group {{group_name}}`

- 获取所有服务的列表：

`getent services`

- 根据 UID 查找用户名：

`getent passwd 1000`

- 执行反向 DNS 查找：

`getent hosts {{host}}`