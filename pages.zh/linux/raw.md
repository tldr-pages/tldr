# raw

> 绑定 Unix 原始字符设备。
> 更多信息：<https://manned.org/raw.8>.

- 将原始字符设备绑定到块设备：

`raw /dev/raw/raw{{1}} {{/dev/block_device}}`

- 查询现有绑定而不是设置新绑定：

`raw /dev/raw/raw{{1}}`

- 查询所有已绑定的原始设备：

`raw {{[-qa|--query --all]}}`