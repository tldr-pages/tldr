# ulimit

> 获取和设置用户限制。
> 更多信息：<https://manned.org/ulimit>。

- 获取所有用户限制的属性：

`ulimit -a`

- 获取同时打开文件的硬限制：

`ulimit -H -n`

- 获取同时打开文件的软限制：

`ulimit -S -n`

- 设置每个用户的最大进程限制：

`ulimit -u 30`