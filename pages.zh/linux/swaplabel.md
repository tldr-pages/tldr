# swaplabel

> 显示或更改交换区域的标签或 UUID。
> 注意：`path/to/file` 可以指向一个常规文件或交换分区。
> 更多信息：<https://manned.org/swaplabel>。

- 显示交换区域的当前标签和 UUID：

`swaplabel {{path/to/file}}`

- 设置交换区域的标签：

`swaplabel {{[-L|--label]}} {{new_label}} {{path/to/file}}`

- 设置交换区域的 UUID（你可以使用 `uuidgen` 生成 UUID）：

`swaplabel {{[-U|--uuid]}} {{new_uuid}} {{path/to/file}}`