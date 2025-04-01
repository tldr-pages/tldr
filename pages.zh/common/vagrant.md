# vagrant

> 管理轻量、可重现和可移植的开发环境。
> 更多信息：<https://www.vagrantup.com>.

- 在当前目录中使用基础 Vagrant 盒创建 Vagrantfile：

`vagrant init`

- 使用来自 HashiCorp Atlas 的 Ubuntu 20.04 (Focal Fossa) 盒创建 Vagrantfile：

`vagrant init ubuntu/focal64`

- 启动并配置 Vagrant 环境：

`vagrant up`

- 暂停机器：

`vagrant suspend`

- 停止机器：

`vagrant halt`

- 通过 SSH 连接到机器：

`vagrant ssh`

- 输出运行中 Vagrant 机器的 SSH 配置文件：

`vagrant ssh-config`

- 列出所有本地盒：

`vagrant box list`