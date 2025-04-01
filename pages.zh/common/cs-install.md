# cs install

> 在安装 `cs` 时配置的安装目录中安装应用程序（要使二进制文件可加载，请在您的 `.bash_profile` 中添加 `$ eval "$(cs install --env)"` 命令）。
> 更多信息：<https://get-coursier.io/docs/cli-install>.

- 安装特定应用程序：

`cs install {{application_name}}`

- 安装特定版本的应用程序：

`cs install {{application_name}}:{{application_version}}`

- 按特定名称搜索应用程序：

`cs search {{application_partial_name}}`

- 如果可用，更新特定应用程序：

`cs update {{application_name}}`

- 更新所有已安装的应用程序：

`cs update`

- 卸载特定应用程序：

`cs uninstall {{application_name}}`

- 列出所有已安装的应用程序：

`cs list`

- 为已安装的应用程序传递特定的 Java 选项：

`{{application_name}} {{-Jjava_option_name1=value1 -Jjava_option_name2=value2 ...}}`
