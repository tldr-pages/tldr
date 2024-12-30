# unix2mac

> 将Unix风格的行结束符转换为macOS风格。
> 将LF替换为CR。
> 另见`unix2dos`、`dos2unix`和`mac2unix`。
> 更多信息：<https://manned.org/unix2mac>。

- 更改文件的行结束符：

`unix2mac {{path/to/file}}`

- 创建一个带有macOS风格行结束符的副本：

`unix2mac {{-n|--newfile}} {{path/to/file}} {{path/to/new_file}}`

- 显示文件信息：

`unix2mac {{-i|--info}} {{path/to/file}}`

- 保留/添加/删除字节顺序标记：

`unix2mac --{{keep-bom|add-bom|remove-bom}} {{path/to/file}}`