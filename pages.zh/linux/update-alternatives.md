# update-alternatives

> 便捷地管理符号链接以确定默认命令。
> 更多信息：<https://manned.org/update-alternatives>。

- 添加符号链接：

`sudo update-alternatives --install {{path/to/symlink}} {{command_name}} {{path/to/command_binary}} {{priority}}`

- 配置 `java` 的符号链接：

`sudo update-alternatives --config {{java}}`

- 移除符号链接：

`sudo update-alternatives --remove {{java}} {{/opt/java/jdk1.8.0_102/bin/java}}`

- 显示指定命令的信息：

`update-alternatives --display {{java}}`

- 显示所有命令及其当前选择：

`update-alternatives --get-selections`