# odps tunnel

> ODPS（开放数据处理服务）中的数据隧道。
> 参见 `odps`。
> 更多信息：<https://www.alibabacloud.com/help/doc-detail/27971.htm>。

- 将表下载到本地文件：

`tunnel download {{table_name}} {{path/to/file}};`

- 将本地文件上传到表的分区：

`tunnel upload {{path/to/file}} {{table_name}}/{{partition_spec}};`

- 上传表时指定字段和记录分隔符：

`tunnel upload {{path/to/file}} {{table_name}} -fd {{field_delim}} -rd {{record_delim}};`

- 使用多个线程上传表：

`tunnel upload {{path/to/file}} {{table_name}} -threads {{num}};`