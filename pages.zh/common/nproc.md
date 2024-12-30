# nproc

> 打印可用的处理单元数量（通常是 CPU）。
> 更多信息：<https://www.gnu.org/software/coreutils/nproc>。

- 显示可用处理单元的数量：

`nproc`

- 显示安装的处理单元数量，包括任何不活动的单元：

`nproc --all`

- 如果可能，从返回值中减去给定数量的单元：

`nproc --ignore {{count}}`