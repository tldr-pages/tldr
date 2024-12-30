# zipsplit

> 将一个 Zip 压缩文件分割成更小的 Zip 压缩文件。
> 更多信息：<https://manned.org/zipsplit>。

- 将 Zip 压缩文件分割成不超过 36000 字节（36 MB）的部分：

`zipsplit {{path/to/archive.zip}}`

- 使用指定的 [n] 字节作为部分限制：

`zipsplit -n {{size}} {{path/to/archive.zip}}`

- 在创建每个部分之间 [p] 暂停：

`zipsplit -p -n {{size}} {{path/to/archive.zip}}`

- 将更小的 Zip 压缩文件输出到指定目录：

`zipsplit -b {{path/to/output_directory}} -n {{size}} {{path/to/archive.zip}}`