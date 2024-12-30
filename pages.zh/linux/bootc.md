# bootc

> 通过容器镜像启动和升级。
> 使用OCI/Docker容器镜像管理事务性、就地操作系统更新。
> 更多信息：<https://containers.github.io/bootc/>.

- 按照在引导加载程序中出现的顺序显示部署：

`bootc status`

- 检查是否有可用的更新：

`bootc upgrade --check`

- 准备一个新的更新并重启进入它：

`bootc upgrade --apply`

- 将操作系统基础更改为新的容器镜像：

`bootc switch {{image}}`

- 重启到之前的ostree部署：

`bootc rollback`