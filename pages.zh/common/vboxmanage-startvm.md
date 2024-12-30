# vboxmanage-startvm

> 启动虚拟机。
> 更多信息：<https://www.virtualbox.org/manual/ch08.html#vboxmanage-startvm>。

- 启动虚拟机：

`VBoxManage startvm {{vm_name|uuid}}`

- 以指定的用户界面模式启动虚拟机：

`VBoxManage startvm {{vm_name|uuid}} --type {{headless|gui|sdl|separate}}`

- 指定密码文件以启动加密虚拟机：

`VBoxManage startvm {{vm_name|uuid}} --password {{path/to/password_file}}`

- 指定密码ID以启动加密虚拟机：

`VBoxManage startvm {{vm_name|uuid}} --password-id {{password_id}}`

- 以环境变量对名称值启动虚拟机：

`VBoxManage startvm {{vm_name|uuid}} --put-env={{name}}={{value}}`