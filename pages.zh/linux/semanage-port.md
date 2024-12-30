# semanage port

> 管理持久的SELinux端口定义。
> 另见：`semanage`。
> 更多信息：<https://manned.org/semanage-port>。

- 列出所有端口标签规则：

`sudo semanage port {{-l|--list}}`

- 列出所有用户定义的端口标签规则，不带标题：

`sudo semanage port {{-l|--list}} {{-C|--locallist}} {{-n|--noheading}}`

- 添加一个用户定义的规则，将标签分配给协议-端口对：

`sudo semanage port {{-a|--add}} {{-t|--type}} {{ssh_port_t}} {{-p|--proto}} {{tcp}} {{22000}}`

- 使用其协议-端口对删除一个用户定义的规则：

`sudo semanage port {{-d|--delete}} {{-p|--proto}} {{udp}} {{11940}}`