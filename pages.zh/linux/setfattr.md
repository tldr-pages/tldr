# setfattr

> 设置扩展文件属性。
> 更多信息：<https://manned.org/setfattr>.

- 为文件设置属性名：

`setfattr -n user.{{attribute_name}} {{path/to/file}}`

- 为文件设置用户自定义的扩展属性值：

`setfattr -n user.{{attribute_name}} -v "{{value}}" {{path/to/file}}`

- 删除文件的特定属性：

`setfattr -x user.{{attribute_name}} {{path/to/file}}`