# virsh pool-define-as

> 根据提供的参数，在 `/etc/libvirt/storage` 目录下为持久虚拟机存储池创建配置文件。
> 参见: `virsh`, `virsh-pool-build`, `virsh-pool-start`。
> 更多信息: <https://manned.org/virsh>。

- 使用 `/var/vms` 作为基础存储系统，为名为 pool_name 的存储池创建配置文件：

`virsh pool-define-as --name {{pool_name}} --type {{dir}} --target {{/var/vms}}`