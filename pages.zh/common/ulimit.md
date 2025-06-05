# ulimit

> 获取和设置用户限制。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-ulimit>.

- 获取所有用户限制的属性：

`ulimit -a`

- 获取同时打开文件数量的硬限制：

`ulimit -H -n`

- 获取同时打开文件数量的软限制：

`ulimit -S -n`

- 设置每个用户的最大进程限制：

`ulimit -u 30`

- 显示帮助信息：

`help ulimit`
