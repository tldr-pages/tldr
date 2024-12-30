# rpm-ostree

> 一种混合镜像/软件包系统。
> 管理 ostree 部署、软件包层、文件系统覆盖和启动配置。
> 更多信息：<https://coreos.github.io/rpm-ostree/administrator-handbook/>.

- 按在引导加载程序中出现的顺序显示 rpm-ostree 部署：

`rpm-ostree status`

- 显示过时且可以更新的软件包：

`rpm-ostree upgrade --preview`

- 准备一个新的 ostree 部署，升级软件包并重启进入该部署：

`rpm-ostree upgrade --reboot`

- 重启进入之前的 ostree 部署：

`rpm-ostree rollback --reboot`

- 在新的 ostree 部署中安装软件包并重启进入该部署：

`rpm-ostree install {{package}} --reboot`