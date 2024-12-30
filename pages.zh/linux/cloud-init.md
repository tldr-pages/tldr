# cloud-init

> 用于管理云实例初始化的命令行工具。
> 更多信息：<https://cloudinit.readthedocs.io>。

- 显示最近一次 cloud-init 运行的状态：

`cloud-init status`

- 等待 cloud-init 完成运行，然后报告状态：

`cloud-init status --wait`

- 列出可用的顶级元数据键以进行查询：

`cloud-init query --list-keys`

- 查询缓存的实例元数据以获取数据：

`cloud-init query {{dot_delimited_variable_path}}`

- 清理日志和工件，以允许 cloud-init 重新运行：

`cloud-init clean`