# f3fix

> 编辑假冒闪存驱动器的分区表。
> 参见：`f3probe`, `f3write`, `f3read`。
> 更多信息：<https://oss.digirati.com.br/f3/>。

- 填充一个假冒的闪存驱动器，使其包含一个与其实际容量相匹配的分区：

`sudo f3fix {{/dev/device_name}}`

- 将分区标记为可启动：

`sudo f3fix --boot {{/dev/device_name}}`

- 指定文件系统类型：

`sudo f3fix --fs-type={{filesystem_type}} {{/dev/device_name}}`
