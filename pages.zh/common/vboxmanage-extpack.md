# vboxmanage-extpack

> 管理Oracle VirtualBox的扩展包。
> 更多信息：<https://www.virtualbox.org/manual/ch08.html#vboxmanage-extpack>。

- 将扩展包安装到VirtualBox（注意：在安装新版本之前，您需要先删除现有版本的扩展包。）：

`VBoxManage extpack install {{path/to/file.vbox-extpack}}`

- 移除现有版本的VirtualBox扩展包：

`VBoxManage extpack install --replace`

- 从VirtualBox中卸载扩展包：

`VBoxManage extpack uninstall {{extension_pack_name}}`

- 卸载扩展包并跳过大多数卸载拒绝：

`VBoxManage extpack uninstall --force {{extension_pack_name}}`

- 清理扩展包留下的临时文件和目录：

`VBoxManage extpack cleanup`