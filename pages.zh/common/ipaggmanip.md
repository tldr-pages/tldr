# ipaggmanip

> 操作由 `ipaggcreate` 生成的聚合统计数据。
> 更多信息：<https://manned.org/ipaggmanip>。

- 合并高位相等的标签：

`ipaggmanip --prefix {{16}} {{path/to/file}}`

- 移除计数小于给定字节数的标签，并输出这些标签的随机样本：

`ipaggmanip --cut-smaller {{100}} --cull-labels {{5}} {{path/to/file}}`

- 如果每个标签的计数非零，则将其计数替换为 1：

`ipaggmanip --posterize {{path/to/file}}`