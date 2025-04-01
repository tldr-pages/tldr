# nova

> OpenStack 项目，用于提供创建计算实例的方法。
> 更多信息：<https://docs.openstack.org/nova/latest/>.

- 列出当前租户的所有虚拟机：

`nova list`

- 列出所有租户的虚拟机（仅限管理员用户）：

`nova list --all-tenants`

- 在特定主机上启动虚拟机：

`nova boot --nic net-id={{net_id}} --image {{image_id}} --flavor {{flavor}} --availability-zone nova:{{host_name}} {{vm_name}}`

- 启动服务器：

`nova start {{server}}`

- 停止服务器：

`nova stop {{server}}`

- 将网络接口附加到特定虚拟机：

`nova interface-attach --net-id {{net_id}} {{server}}`