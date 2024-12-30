# dvc 配置

> 用于管理 dvc 仓库自定义配置选项的低级命令。
> 这些配置可以在项目、本地、全局或系统级别进行设置。
> 更多信息请访问: <https://dvc.org/doc/command-reference/config>。

- 获取默认远程的名称：

`dvc config core.remote`

- 设置项目的默认远程：

`dvc config core.remote {{remote_name}}`

- 取消设置项目的默认远程：

`dvc config --unset core.remote`

- 获取当前项目指定键的配置值：

`dvc config {{key}}`

- 在项目级别设置键的配置值：

`dvc config {{key}} {{value}}`

- 取消设置给定键的项目级别配置值：

`dvc config --unset {{key}}`

- 设置本地、全局或系统级别的配置值：

`dvc config --{{local|global|system}} {{key}} {{value}}`