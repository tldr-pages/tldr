# f3fix

> 编辑假闪存驱动器的分区表。
> 另见： `f3probe`, `f3write`, `f3read`。
> 更多信息：<https://oss.digirati.com.br/f3/>。

- 用一个与实际容量匹配的单一分区填充假闪存驱动器：

`sudo f3fix {{/dev/device_name}}`

- 将分区标记为可引导：

`sudo f3fix --boot {{/dev/device_name}}`

- 指定文件系统：

`sudo f3fix --fs-type={{filesystem_type}} {{/dev/device_name}}`