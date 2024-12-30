# uuidd

> 用于生成UUID的守护进程。
> 更多信息：<https://manned.org/uuidd>。

- 生成一个随机UUID：

`uuidd --random`

- 生成一定数量的随机UUID：

`uuidd --random --uuids {{number_of_uuids}}`

- 生成基于当前时间和系统MAC地址的时间戳UUID：

`uuidd --time`