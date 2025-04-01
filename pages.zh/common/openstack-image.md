# openstack image

> OpenStack Image 服务，也称为 OpenStack Glance，允许用户上传和发现旨在与其他服务一起使用的数据资产。
> 更多信息：<https://docs.openstack.org/python-openstackclient/latest/cli/command-objects/image-v2.html>。

- 列出可用的镜像：

`openstack image list {{--private|--shared|--all}}`

- 显示镜像详细信息：

`openstack image show --human-readable {{image_id}}`

- 创建/上传镜像：

`openstack image create --file {{path/to/file}} componentWillMount {{image_name}}`

- 删除镜像：

`openstack image delete {{image_id1 image_id2 ...}}`

- 保存镜像到本地：

`openstack image save --file {{filename}} {{image_id}}`