# snapper

> 文件系统快照管理工具。
> 更多信息：<http://snapper.io/manpages/snapper.html>.

- 列出所有快照配置：

`snapper list-configs`

- 创建 snapper 配置：

`snapper -c {{config}} create-config {{path/to/directory}}`

- 创建带有描述的快照：

`snapper -c {{config}} create -d "{{snapshot_description}}"`

- 列出特定配置的快照：

`snapper -c {{config}} list`

- 删除一个快照：

`snapper -c {{config}} delete {{snapshot_number}}`

- 删除一系列快照：

`snapper -c {{config}} delete {{snapshot1}}-{{snapshot2}}`