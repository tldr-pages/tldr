# dvc config

> 管理 DVC 仓库的自定义配置选项的低级命令。
> 这些配置可以是项目级别、本地级别、全局级别或系统级别。
> 更多信息：<https://dvc.org/doc/command-reference/config>.

- 获取默认远程仓库的名称：

`dvc config core.remote`

- 设置项目的默认远程仓库：

`dvc config core.remote {{remote_name}}`

- 取消设置项目的默认远程仓库：

`dvc config --unset core.remote`

- 获取当前项目中指定键的配置值：

`dvc config {{key}}`

- 设置项目级别的键的配置值：

`dvc config {{key}} {{value}}`

- 取消设置项目级别的指定键的配置值：

`dvc config --unset {{key}}`

- 设置本地、全局或系统级别的配置值：

`dvc config --{{local|global|system}} {{key}} {{value}}`