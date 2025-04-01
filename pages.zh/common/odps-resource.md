# odps resource

> 管理 ODPS（开放数据处理服务）中的资源。
> 参见 `odps`。
> 更多信息：<https://www.alibabacloud.com/help/doc-detail/27971.htm>。

- 显示当前项目中的资源：

`list resources;`

- 添加文件资源：

`add file {{filename}} as {{alias}};`

- 添加归档资源：

`add archive {{archive.tar.gz}} as {{alias}};`

- 添加 .jar 资源：

`add jar {{package.jar}};`

- 添加 .py 资源：

`add py {{script.py}};`

- 删除资源：

`drop resource {{resource_name}};`