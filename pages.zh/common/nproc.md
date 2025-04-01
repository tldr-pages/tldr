# nproc

> 打印可用处理单元（通常是 CPU）的数量。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/nproc-invocation.html>.

- 显示可用处理单元的数量：

`nproc`

- 显示安装的处理单元数量，包括任何不活跃的单元：

`nproc --all`

- 如可能，从返回值中减去指定数量的单元：

`nproc --ignore {{count}}`
