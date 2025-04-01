# odps

> 阿里云 ODPS（开放数据处理服务）命令行工具。
> 某些子命令（如 `inst`）有自己的使用文档。
> 更多信息：<https://www.alibabacloud.com/help/doc-detail/27971.htm>。

- 使用自定义配置文件启动命令行：

`odpscmd --config={{odps_config.ini}}`

- 切换当前项目：

`use {{project_name}};`

- 显示当前项目中的表：

`show tables;`

- 描述表：

`desc {{table_name}};`

- 显示表的分区：

`show partitions {{table_name}};`

- 描述分区：

`desc {{table_name}} partition ({{partition_spec}});`
