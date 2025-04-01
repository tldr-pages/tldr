# bpkg

> Bash 脚本的包管理器。
> 更多信息：<https://github.com/bpkg/bpkg>。

- 更新本地索引：

`bpkg update`

- 全局安装一个包：

`bpkg install --global {{package}}`

- 在当前目录的子目录中安装一个包：

`bpkg install {{package}}`

- 全局安装指定版本的包：

`bpkg install {{package}}@{{version}} -g`

- 显示特定包的详细信息：

`bpkg show {{package}}`

- 运行一个命令，可选指定其参数：

`bpkg run {{command}} {{argument1 argument2 ...}}`