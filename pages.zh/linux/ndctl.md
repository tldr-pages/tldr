# ndctl

> 管理非易失性DIMM的工具。
> 更多信息：<https://manned.org/ndctl>。

- 创建一个 'fsdax' 模式的命名空间：

`ndctl create-namespace --mode={{fsdax}}`

- 将命名空间的模式更改为 'raw'：

`ndctl create-namespace --reconfigure={{namespaceX.Y}} --mode={{raw}}`

- 检查一个扇区模式的命名空间的一致性，并在需要时进行修复：

`ndctl check-namespace --repair {{namespaceX.Y}}`

- 列出所有命名空间、区域和总线（包括禁用的）：

`ndctl list --namespaces --regions --buses --idle`

- 列出特定的命名空间并包含大量额外信息：

`ndctl list -vvv --namespace={{namespaceX.Y}}`

- 运行监视器以观察 'ACPI.NFIT' 总线上NVDIMM的SMART健康事件：

`ndctl monitor --bus={{ACPI.NFIT}}`

- 删除命名空间（如适用）或将其重置为初始状态：

`ndctl destroy-namespace --force {{namespaceX.Y}}`