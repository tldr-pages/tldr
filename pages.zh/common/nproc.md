# nproc

> 打印可用的处理单元（通常是 CPU）数量。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/nproc-invocation.html>。

- 显示可用的处理单元数量：

`nproc`

- 显示已安装的处理单元数量，包括非活动的：

`nproc --all`

- 如果可能，从返回值中减去给定数量的单元：

`nproc --ignore {{数量}}`
