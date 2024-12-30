# 原始

> 绑定一个Unix原始字符设备。
> 更多信息：<https://manned.org/raw.8>。

- 将一个原始字符设备绑定到块设备：

`raw /dev/raw/raw{{1}} {{/dev/block_device}}`

- 查询现有的绑定而不是设置一个新的绑定：

`raw /dev/raw/raw{{1}}`

- 查询所有已绑定的原始设备：

`raw -qa`