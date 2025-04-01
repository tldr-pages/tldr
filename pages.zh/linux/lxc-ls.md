# lxc-ls

> 列出 Linux 容器。
> 更多信息：<https://linuxcontainers.org/lxc/manpages/man1/lxc-ls.1.html>.

- 列出所有容器：

`sudo lxc-ls`

- 列出活动容器（包括冻结和运行中的）：

`sudo lxc-ls --active`

- 列出仅冻结的容器：

`sudo lxc-ls --frozen`

- 列出仅停止的容器：

`sudo lxc-ls --stopped`

- 以花哨的、基于列的格式列出容器：

`sudo lxc-ls {{[-f|--fancy]}}`

- 显示帮助：

`lxc-ls {{[-?|--help]}}`