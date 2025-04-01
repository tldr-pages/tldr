# semanage boolean

> 管理持久的 SELinux 布尔设置。
> 有关更多信息，请参见：`semanage` 用于管理 SELinux 策略，`getsebool` 用于检查布尔值，`setsebool` 用于应用非持久的布尔设置。
> 更多信息：<https://manned.org/semanage-boolean>.

- 列出所有布尔设置：

`sudo semanage boolean {{[-l|--list]}}`

- 列出所有用户定义的布尔设置，不显示标题：

`sudo semanage boolean {{[-l|--list]}} {{[-C|--locallist]}} {{[-n|--noheading]}}`

- 持久设置或取消设置一个布尔值：

`sudo semanage boolean {{[-m|--modify]}} {{-1|--on|-0|--off}} {{haproxy_connect_any}}`
