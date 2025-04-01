# semanage port

> 管理持久的 SELinux 端口定义。
> 参见：`semanage`。
> 更多信息：<https://manned.org/semanage-port>。

- 列出所有端口标签规则：

`sudo semanage port {{[-l|--list]}}`

- 列出所有用户定义的端口标签规则，不显示标题：

`sudo semanage port {{[-l|--list]}} {{[-C|--locallist]}} {{[-n|--noheading]}}`

- 添加一个用户定义的规则，为协议-端口对分配标签：

`sudo semanage port {{[-a|--add]}} {{[-t|--type]}} {{ssh_port_t}} {{[-p|--proto]}} {{tcp}} {{22000}}`

- 添加一个用户定义的规则，为协议-端口范围对分配标签：

`sudo semanage port {{[-a|--add]}} {{[-t|--type]}} {{http_port_t}} {{[-p|--proto]}} {{tcp}} {{80-88}}`

- 使用协议-端口对删除一个用户定义的规则：

`sudo semanage port {{[-d|--delete]}} {{[-p|--proto]}} {{udp}} {{11940}}`
