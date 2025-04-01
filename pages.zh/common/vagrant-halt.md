# vagrant halt

> 关闭 Vagrant 管理的正在运行的虚拟机。
> 参见: `vagrant`, `vagrant box`, `vagrant plugin`, `vagrant validate`。
> 更多信息：<https://developer.hashicorp.com/vagrant/docs/cli/halt>。

- 优雅地关闭当前正在运行的 Vagrant 虚拟机：

`vagrant halt`

- 通过 ID 或名称优雅地关闭特定的虚拟机：

`vagrant halt {{id_or_name}}`

- 强制关闭当前正在运行的虚拟机（如果它们属于同一个 Vagrant 环境，这可能会影响多个正在运行的虚拟机）：

`vagrant halt {{[-f|--force]}}`

- 强制关闭特定的虚拟机，通过其 ID 或名称：

`vagrant halt {{[-f|--force]}} {{id_or_name}}`