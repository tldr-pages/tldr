# swaplabel

> 打印或更改交换区的标签或 UUID。
> 注意：`path/to/file` 可以指向常规文件或交换分区。
> 更多信息：<https://manned.org/swaplabel>。

- 显示交换区的当前标签和 UUID：

`swaplabel {{path/to/file}}`

- 设置交换区的标签：

`swaplabel --label {{new_label}} {{path/to/file}}`

- 设置交换区的 UUID（您可以使用 `uuidgen` 生成 UUID）：

`swaplabel --uuid {{new_uuid}} {{path/to/file}}`