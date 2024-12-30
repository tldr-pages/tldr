# ansible

> 通过 SSH 远程管理计算机组。（使用 `/etc/ansible/hosts` 文件添加新组/主机）。
> 一些子命令如 `galaxy` 有自己的使用文档。
> 更多信息：<https://www.ansible.com/>。

- 列出属于某个组的主机：

`ansible {{group}} --list-hosts`

- 通过调用 ping [模块] 向一组主机发送 Ping：

`ansible {{group}} -m ping`

- 通过调用 setup [模块] 显示有关一组主机的信息：

`ansible {{group}} -m setup`

- 通过调用命令模块并传递参数在一组主机上执行命令：

`ansible {{group}} -m command -a '{{my_command}}'`

- 以管理员权限执行命令：

`ansible {{group}} --become --ask-become-pass -m command -a '{{my_command}}'`

- 使用自定义清单文件执行命令：

`ansible {{group}} -i {{inventory_file}} -m command -a '{{my_command}}'`

- 列出清单中的组：

`ansible localhost -m debug -a '{{var=groups.keys()}}'`