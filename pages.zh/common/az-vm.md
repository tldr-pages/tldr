# az vm

> 管理 Azure 中的虚拟机。
> `azure-cli` 的一部分（也称为 `az`）。
> 更多信息：<https://learn.microsoft.com/cli/azure/vm>.

- 以表格形式显示可用的虚拟机列表：

`az vm list --output table`

- 使用默认的 Ubuntu 镜像创建一个虚拟机并生成 SSH 密钥：

`az vm create {{[-g|--resource-group]}} {{rg}} {{[-n|--name]}} {{vm_name}} --image {{UbuntuLTS}} --admin-user {{azureuser}} --generate-ssh-keys`

- 停止一个虚拟机：

`az vm stop {{[-g|--resource-group]}} {{rg}} {{[-n|--name]}} {{vm_name}}`

- 释放一个虚拟机（解除分配）：

`az vm deallocate {{[-g|--resource-group]}} {{rg}} {{[-n|--name]}} {{vm_name}}`

- 启动一个虚拟机：

`az vm start {{[-g|--resource-group]}} {{rg}} {{[-n|--name]}} {{vm_name}}`

- 重启一个虚拟机：

`az vm restart {{[-g|--resource-group]}} {{rg}} {{[-n|--name]}} {{vm_name}}`

- 列出 Azure Marketplace 中可用的虚拟机镜像：

`az vm image list`
