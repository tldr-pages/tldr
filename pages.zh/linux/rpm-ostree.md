# rpm-ostree

> 一个混合的镜像/包系统。
> 管理 ostree 部署、包层、文件系统覆盖和启动配置。
> 更多信息：<https://coreos.github.io/rpm-ostree/administrator-handbook/>。

- 按照它们在引导加载程序中的顺序显示 rpm-ostree 部署：

`rpm-ostree status`

- 显示可以更新的过时包：

`rpm-ostree upgrade --preview`

- 准备一个新的 ostree 部署，包含已更新的包，并重启进入该部署：

`rpm-ostree upgrade --reboot`

- 重启进入上一个 ostree 部署：

`rpm-ostree rollback --reboot`

- 在新的 ostree 部署中安装一个包并重启进入该部署：

`rpm-ostree install {{package}} --reboot`
