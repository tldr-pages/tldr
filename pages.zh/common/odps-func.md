# odps func

> 管理 ODPS (开放数据处理服务) 中的函数。
> 参见 `odps`。
> 更多信息：<https://www.alibabacloud.com/help/doc-detail/27971.htm>。

- 显示当前项目中的函数：

`list functions;`

- 使用 `.jar` 资源创建 Java 函数：

`create function {{func_name}} as {{path.to.package.Func}} using '{{package.jar}}';`

- 使用 `.py` 资源创建 Python 函数：

`create function {{func_name}} as {{script.Func}} using '{{script.py}}';`

- 删除函数：

`drop function {{func_name}};`
