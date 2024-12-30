# Vagrant

> 管理轻量级、可重现和可移植的开发环境。
> 更多信息：<https://www.vagrantup.com>。

- 在当前目录创建一个包含基础 Vagrant box 的 Vagrantfile：

`vagrant init`

- 使用来自 HashiCorp Atlas 的 Ubuntu 20.04（Focal Fossa）box 创建 Vagrantfile：

`vagrant init ubuntu/focal64`

- 启动并配置 Vagrant 环境：

`vagrant up`

- 挂起虚拟机：

`vagrant suspend`

- 停止虚拟机：

`vagrant halt`

- 通过 SSH 连接到虚拟机：

`vagrant ssh`

- 输出正在运行的 Vagrant 虚拟机的 SSH 配置文件：

`vagrant ssh-config`

- 列出所有本地 boxes：

`vagrant box list`