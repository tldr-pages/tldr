# cs 安装

> 在安装 `cs` 时配置的安装目录中安装应用程序（要使二进制文件可加载，请将 `$ eval "$(cs install --env)"` 命令添加到你的 `.bash_profile` 中）。
> 更多信息：<https://get-coursier.io/docs/cli-install>。

- 安装特定应用程序：

`cs install {{应用程序名称}}`

- 安装特定版本的应用程序：

`cs install {{应用程序名称}}:{{应用程序版本}}`

- 按特定名称搜索应用程序：

`cs search {{应用程序部分名称}}`

- 如果可用，更新特定应用程序：

`cs update {{应用程序名称}}`

- 更新所有已安装的应用程序：

`cs update`

- 卸载特定应用程序：

`cs uninstall {{应用程序名称}}`

- 列出所有已安装的应用程序：

`cs list`

- 向已安装的应用程序传递特定的 Java 选项：

`{{应用程序名称}} {{-Jjava_option_name1=value1 -Jjava_option_name2=value2 ...}}`