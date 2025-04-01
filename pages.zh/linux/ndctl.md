# ndctl

> 用于管理非易失性双列直插内存模块 (NVDIMM) 的工具。
> 更多信息：<https://manned.org/ndctl>。

- 创建一个 'fsdax' 模式的名字空间：

`ndctl create-namespace --mode={{fsdax}}`

- 将名字空间的模式更改为 'raw'：

`ndctl create-namespace --reconfigure={{namespaceX.Y}} --mode={{raw}}`

- 检查扇区模式的名字空间的一致性，并在必要时进行修复：

`ndctl check-namespace --repair {{namespaceX.Y}}`

- 列出所有名字空间、区域和总线（包括已禁用的）：

`ndctl list --namespaces --regions --buses --idle`

- 列出特定的名字空间并包含大量附加信息：

`ndctl list -vvv --namespace={{namespaceX.Y}}`

- 运行一个监控器，以监控 'ACPI.NFIT' 总线上 NVDIMM 的 SMART 健康事件：

`ndctl monitor --bus={{ACPI.NFIT}}`

- 移除一个名字空间（如适用）或将其重置为初始状态：

`ndctl destroy-namespace --force {{namespaceX.Y}}`