# multipass

> 使用原生管理程序管理 Ubuntu 虚拟机。
> 更多信息：<https://multipass.run/>.

- 列出可用于启动实例的别名：

`multipass find`

- 启动新实例，设置其名称并使用 cloud-init 配置文件：

`multipass launch -n {{instance_name}} --cloud-init {{configuration_file}}`

- 列出所有已创建的实例及其部分属性：

`multipass list`

- 通过名称启动特定实例：

`multipass start {{instance_name}}`

- 显示实例的属性：

`multipass info {{instance_name}}`

- 通过名称在特定实例上打开 shell 提示符：

`multipass shell {{instance_name}}`

- 通过名称删除实例：

`multipass delete {{instance_name}}`

- 将目录挂载到特定实例：

`multipass mount {{path/to/local/directory}} {{instance_name}}:{{path/to/target/directory}}`