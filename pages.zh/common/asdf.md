# asdf

> 用于管理不同软件包版本的命令行界面。
> 更多信息：<https://asdf-vm.com>。

- 列出所有可用的插件：

`asdf plugin list all`

- 安装一个插件：

`asdf plugin add {{name}}`

- 列出一个软件包的所有可用版本：

`asdf list all {{name}}`

- 安装一个特定版本的软件包：

`asdf install {{name}} {{version}}`

- 设置软件包的全局版本：

`asdf global {{name}} {{version}}`

- 设置软件包的本地版本：

`asdf local {{name}} {{version}}`