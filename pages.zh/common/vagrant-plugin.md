# vagrant plugin

> 管理 Vagrant 插件。
> 参见：`vagrant`。
> 更多信息：<https://developer.hashicorp.com/vagrant/docs/cli/plugin>。

- 列出所有已安装的插件：

`vagrant plugin list`

- 从远程仓库（通常是 RubyGems）安装插件：

`vagrant plugin install {{vagrant_vbguest}}`

- 从本地文件源安装插件：

`vagrant plugin install {{path/to/my_plugin.gem}}`

- 将所有已安装的插件更新到最新版本：

`vagrant plugin update`

- 将特定插件更新到最新版本：

`vagrant plugin update {{vagrant_vbguest}}`

- 卸载特定插件：

`vagrant plugin uninstall {{vagrant_vbguest}}`