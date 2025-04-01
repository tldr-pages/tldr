# bootc

> 通过容器镜像进行启动和升级。
> 使用 OCI/Docker 容器镜像管理事务性的、就地操作系统的更新。
> 更多信息：<https://containers.github.io/bootc/>.

- 按照它们在引导加载程序中出现的顺序显示部署：

`bootc status`

- 检查是否有可用的更新：

`bootc upgrade --check`

- 准备新的更新并重启进入：

`bootc upgrade --apply`

- 将操作系统基础切换到新的容器镜像：

`bootc switch {{image}}`

- 重启到上一个 ostree 部署：

`bootc rollback`