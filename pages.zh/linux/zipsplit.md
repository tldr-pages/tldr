# zipsplit

> 将 Zip 压缩包拆分成多个较小的 Zip 压缩包。
> 更多信息：<https://manned.org/zipsplit>。

- 将 Zip 压缩包拆分成最大不超过 36000 字节（36 MB）的部分：

`zipsplit {{path/to/archive.zip}}`

- 使用指定的 [n] 字节数作为部分的大小限制：

`zipsplit -n {{size}} {{path/to/archive.zip}}`

- 在创建每个部分之间 [p] 暂停：

`zipsplit -p -n {{size}} {{path/to/archive.zip}}`

- 将较小的 Zip 压缩包输出到指定的目录：

`zipsplit -b {{path/to/output_directory}} -n {{size}} {{path/to/archive.zip}}`
