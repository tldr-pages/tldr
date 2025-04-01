# az vm

> 管理 Azure 中的虚拟机。
> 作为 `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/vm>.

- 显示可用虚拟机的表格：

`az vm list --output table`

- 使用默认的 Ubuntu 镜像创建虚拟机并生成 SSH 密钥：

`az vm create --resource-group {{rg}} --name {{vm_name}} --image {{UbuntuLTS}} --admin-user {{azureuser}} --generate-ssh-keys`

- 停止虚拟机：

`az vm stop --resource-group {{rg}} --name {{vm_name}}`

- 释放虚拟机：

`az vm deallocate --resource-group {{rg}} --name {{vm_name}}`

- 启动虚拟机：

`az vm start --resource-group {{rg}} --name {{vm_name}}`

- 重启虚拟机：

`az vm restart --resource-group {{rg}} --name {{vm_name}}`

- 列出 Azure 市场中可用的虚拟机镜像：

`az vm image list`
