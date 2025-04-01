# openstack server

> 管理 OpenStack 虚拟机。
> OpenStack 计算服务，也称为 OpenStack Nova，主要托管和管理云计算系统。
> 更多信息：<https://docs.openstack.org/python-openstackclient/latest/cli/command-objects/server.html>.

- 列出服务器：

`openstack server list`

- 启动服务器：

`openstack server start {{instance_id1 instance_id2 ...}}`

- 停止服务器：

`openstack server stop {{instance_id1 instance_id2 ...}}`

- 创建新服务器：

`openstack server create --image {{image_id}} --flavor {{flavor_id}} --network {{network_id}} --wait {{server_name}}`

- 删除服务器：

`openstack server delete {{instance_id1 instance_id2 ...}}`

- 将服务器迁移到不同的主机：

`openstack server migrate --live {{host_hostname}} '{{--shared-migration|--block-migration}}' --wait {{instance_id}}`

- 对服务器执行软重启或硬重启：

`openstack server reboot '{{--soft|--hard}}' --wait {{instance_id}}`
