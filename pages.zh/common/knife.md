# 刀具

> 从本地 Chef 仓库与 Chef 服务器交互。
> 更多信息：<https://docs.chef.io/knife.html>。

- 引导一个新节点：

`knife bootstrap {{fqdn_or_ip}}`

- 列出所有注册的节点：

`knife node list`

- 查看一个节点：

`knife node show {{node_name}}`

- 编辑一个节点：

`knife node edit {{node_name}}`

- 编辑一个角色：

`knife role edit {{role_name}}`

- 查看一个数据包：

`knife data bag show {{data_bag_name}} {{data_bag_item}}`

- 将本地食谱上传到 Chef 服务器：

`knife cookbook upload {{cookbook_name}}`