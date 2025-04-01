# vboxmanage-registervm

> 注册虚拟机（VM）。
> 更多信息：<https://www.virtualbox.org/manual/ch08.html#vboxmanage-registervm>。

- 注册已存在的虚拟机：

`VBoxManage registervm {{path/to/filename.vbox}}`

- 提供虚拟机的加密密码文件：

`VBoxManage registervm {{path/to/filename.vbox}} --password {{path/to/password_file}}`

- 在命令行中提示输入加密密码：

`VBoxManage registervm {{path/to/filename.vbox}} --password -`