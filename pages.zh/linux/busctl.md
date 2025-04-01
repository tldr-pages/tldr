# busctl

> 检查和监控 D-Bus 总线。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/busctl.html>.

- 显示总线上的所有对等服务，以服务名称表示：

`busctl list`

- 显示总线服务、进程或总线所有者（如果未指定参数）的进程信息和凭证：

`busctl status {{service|pid}}`

- 转储正在交换的消息。如果未指定服务，则显示总线上的所有消息：

`busctl monitor {{service1 service2 ...}}`

- 显示一个或多个服务的对象树（如果未指定服务，则显示所有服务的对象树）：

`busctl tree {{service1 service2 ...}}`

- 显示指定服务上指定对象的接口、方法、属性和信号：

`busctl introspect {{service}} {{path/to/object}}`

- 检索一个或多个对象属性的当前值：

`busctl get-property {{service}} {{path/to/object}} {{interface_name}} {{property_name}}`

- 调用一个方法并显示响应：

`busctl call {{service}} {{path/to/object}} {{interface_name}} {{method_name}}`
