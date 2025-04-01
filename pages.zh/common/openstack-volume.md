# openstack volume

> 管理 OpenStack 卷。
> OpenStack 块存储服务（又称 OpenStack Cinder）为 Nova 虚拟机、Ironic 裸金属主机、容器等提供卷。
> 更多信息：<https://docs.openstack.org/python-openstackclient/latest/cli/command-objects/volume.html>。

- 列出所有卷：

`openstack volume list --all-projects`

- 显示卷详细信息：

`openstack volume show {{volume_id}}`

- 创建新卷：

`openstack volume create --size {{size_in_GB}} --image {{image_id}} --snapshot {{snapshot_id}} {{--bootable|--non-bootable}} {{volume_name}}`

- 删除卷：

`openstack volume delete {{volume_id1 volume_id2 ...}}`

- 将卷迁移到新主机：

`openstack volume migrate --host {{host_hostname}} {{instance_id}}`

- 设置卷属性：

`openstack volume set --name {{volume_new_name}} --size {{volume_new_size}} {{--attached|--detached}} {{--bootable|--non-bootable}} {{volume_id}}`
