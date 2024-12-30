# semanage boolean

> 管理持久的 SELinux 布尔设置。
> 另请参阅：用于管理 SELinux 策略的 `semanage`，用于检查布尔值的 `getsebool`，以及用于应用非持久布尔设置的 `setsebool`。
> 更多信息：<https://manned.org/semanage-boolean>。

- 列出所有布尔设置：

`sudo semanage boolean {{-l|--list}}`

- 列出所有用户定义的布尔设置，且不带标题：

`sudo semanage boolean {{-l|--list}} {{-C|--locallist}} {{-n|--noheading}}`

- 持久地设置或取消布尔设置：

`sudo semanage boolean {{-m|--modify}} {{-1|--on|-0|--off}} {{haproxy_connect_any}}`