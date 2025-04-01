# ipaggmanip

> 操作由 `ipaggcreate` 生成的聚合统计信息。
> 更多信息：<https://manned.org/ipaggmanip>.

- 合并在高阶位相同的标签：

`ipaggmanip --prefix {{16}} {{path/to/file}}`

- 删除计数小于指定字节数的标签，并输出这些标签的随机样本：

`ipaggmanip --cut-smaller {{100}} --cull-labels {{5}} {{path/to/file}}`

- 如果标签的计数非零，则将其计数替换为 1：

`ipaggmanip --posterize {{path/to/file}}`