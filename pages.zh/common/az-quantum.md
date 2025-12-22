# az quantum

> 管理 Azure Quantum 工作区并向提供商提交量子作业（预览版，需要 quantum 扩展）。
> 更多信息：<https://learn.microsoft.com/cli/azure/quantum>.

- 创建一个新的 Azure Quantum 工作区：

`az quantum workspace create {{[-g|--resource-group]}} {{资源组}} {{[-l|--location]}} {{位置}} {{[-w|--workspace-name]}} {{工作区}} {{[-a|--storage-account]}} {{我的存储帐户名称}}`

- 列出所有 Azure Quantum 工作区：

`az quantum workspace list`

- 设置默认的 Azure Quantum 工作区：

`az quantum workspace set {{[-g|--resource-group]}} {{资源组}} {{[-w|--workspace-name]}} {{工作区}}`

- 向目标提交一个 QIR 量子作业：

`az quantum job submit {{[-g|--resource-group]}} {{资源组}} {{[-w|--workspace-name]}} {{工作区}} {{[-l|--location]}} {{位置}} {{[-t|--target-id]}} {{ID}} --job-name {{作业}} --job-input-file {{QIR 位码.bc}} --job-input-format {{qir.v1}}`

- 列出某个 Quantum 工作区中的所有作业：

`az quantum job list {{[-g|--resource-group]}} {{资源组}} {{[-l|--location]}} {{位置}} {{[-w|--workspace-name]}} {{工作区}}`

- 获取量子作业的输出：

`az quantum job output {{[-g|--resource-group]}} {{资源组}} {{[-w|--workspace-name]}} {{工作区}} --job-id {{作业}}`

- 列出某个位置中可用的提供商产品：

`az quantum offerings list {{[-l|--location]}} {{位置}}`

- 设置提交作业时使用的默认目标：

`az quantum target set {{[-t|--target-id]}} {{ID}}`
