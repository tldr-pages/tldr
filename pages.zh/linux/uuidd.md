# uuidd

> 生成 UUID 的守护进程。
> 更多信息：<https://manned.org/uuidd>。

- 生成一个随机的 UUID：

`uuidd --random`

- 生成指定数量的随机 UUID：

`uuidd --random --uuids {{number_of_uuids}}`

- 生成基于当前时间和系统 MAC 地址的时间戳 UUID：

`uuidd --time`