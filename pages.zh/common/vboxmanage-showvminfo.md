# vboxmanage-showvminfo

> 显示已注册虚拟机的信息。
> 更多信息：<https://www.virtualbox.org/manual/ch08.html#vboxmanage-showvminfo>。

- 显示特定虚拟机的信息：

`VBoxManage showvminfo {{vm_name|uuid}}`

- 显示特定虚拟机的详细信息：

`VBoxManage showvminfo --details {{vm_name|uuid}}`

- 以机器可读格式显示信息：

`VBoxManage showvminfo --machinereadable {{vm_name|uuid}}`

- 如果虚拟机已加密，指定密码ID：

`VBoxManage showvminfo --password-id {{password_id}} {{vm_name|uuid}}`

- 如果虚拟机已加密，指定密码文件：

`VBoxManage showvminfo --password {{path/to/password_file}} {{vm_name|uuid}}`

- 显示特定虚拟机的日志：

`VBoxManage showvminfo --log {{vm_name|uuid}}`