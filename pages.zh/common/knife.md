# knife

> 与本地 Chef 仓库中的 Chef 服务器交互。
> 更多信息：<https://docs.chef.io/knife.html>。

- 引导新节点：

`knife bootstrap {{fqdn_or_ip}}`

- 列出所有已注册的节点：

`knife node list`

- 显示节点信息：

`knife node show {{node_name}}`

- 编辑节点：

`knife node edit {{node_name}}`

- 编辑角色：

`knife role edit {{role_name}}`

- 查看数据包：

`knife data bag show {{data_bag_name}} {{data_bag_item}}`

- 将本地cookbook上传到Chef服务器：

`knife cookbook upload {{cookbook_name}}`