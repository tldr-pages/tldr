# vagrant validate

> 检查 Vagrantfile 的有效性。
> 参见：`vagrant`，`vagrant box`，`vagrant plugin`。
> 更多信息：<https://developer.hashicorp.com/vagrant/docs/cli/validate>。

- 检查 Vagrantfile 的语法，确保其结构正确且无错误：

`vagrant validate`

- 检查 Vagrantfile 的结构正确性，同时忽略特定提供程序的配置选项：

`vagrant validate {{[-p|--ignore-provider]}} {{docker|hyperv|libvirt|parallels|qemu|virtualbox|vmware_desktop}}`
