# getfattr

> 显示文件名和扩展属性。
> 更多信息：<https://manned.org/getfattr>.

- 获取文件的所有扩展属性并以详细格式显示：

`getfattr -d {{path/to/file}}`

- 获取文件的特定属性：

`getfattr -n user.{{attribute_name}} {{path/to/file}}`