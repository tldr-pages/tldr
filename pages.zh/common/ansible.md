# ansible

> 通过 SSH 协议远程管理计算机组。使用 `/etc/ansible/hosts` 文件来添加组 / 主机。
> 此命令也有关于其子命令的文件，例如：`galaxy`.
> 更多信息：<https://docs.ansible.com/ansible/latest/cli/ansible.html>.

- 列出给定组下的所有主机：

`ansible {{组}} --list-hosts`

- 调用 ping 模块来 ping 一组主机：

`ansible {{组}} {{[-m|--module-name]}} ping`

- 通过调用安装模块来显示关于一组主机的信息：

`ansible {{组}} {{[-m|--module-name]}} setup`

- 调用命令模块并使用给定的参数来对一组主机执行命令：

`ansible {{组}} {{[-m|--module-name]}} command {{[-a|--args]}} '{{命令}}'`

- 以管理员权限执行一个命令：

`ansible {{组}} {{[-b|--become]}} --ask-become-pass {{[-m|--module-name]}} command {{[-a|--args]}} '{{命令}}'`

- 使用自定义的清单文件执行一个命令：

`ansible {{组}} {{[-i|--inventory]}} {{清单文件}} {{[-m|--module-name]}} command {{[-a|--args]}} '{{命令}}'`

- 列出清单中的组：

`ansible localhost {{[-m|--module-name]}} debug {{[-a|--args]}} '{{var=groups.keys()}}'`
