# vboxmanage-extpack

> 管理 Oracle VirtualBox 的扩展包。
> 更多信息：<https://www.virtualbox.org/manual/ch08.html#vboxmanage-extpack>。

- 安装扩展包到 VirtualBox（注意：在安装新版本之前，需要卸载已存在的扩展包版本）：

`VBoxManage extpack install {{path/to/file.vbox-extpack}}`

- 卸载 VirtualBox 扩展包的现有版本：

`VBoxManage extpack install --replace`

- 从 VirtualBox 卸载扩展包：

`VBoxManage extpack uninstall {{extension_pack_name}}`

- 卸载扩展包并跳过大部分卸载拒绝：

`VBoxManage extpack uninstall --force {{extension_pack_name}}`

- 清理扩展包留下的临时文件和目录：

`VBoxManage extpack cleanup`