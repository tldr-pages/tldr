# odps 实例

> 管理 ODPS（开放数据处理服务）中的实例。
> 另见 `odps`。
> 更多信息：<https://www.alibabacloud.com/help/doc-detail/27971.htm>。

- 显示当前用户创建的实例：

`show instances;`

- 描述一个实例的详细信息：

`desc instance {{instance_id}};`

- 检查一个实例的状态：

`status {{instance_id}};`

- 等待一个实例的终止，直到那时打印日志和进度信息：

`wait {{instance_id}};`

- 杀死一个实例：

`kill {{instance_id}};`