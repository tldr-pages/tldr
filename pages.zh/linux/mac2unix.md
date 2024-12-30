# mac2unix

> 将 macOS 风格的行结束符转换为 Unix 风格。
> 将 CR 替换为 LF。
> 另请参见 `unix2dos`、`unix2mac` 和 `dos2unix`。
> 更多信息：<https://manned.org/mac2unix>。

- 更改文件的行结束符：

`mac2unix {{path/to/file}}`

- 创建一个带有 Unix 风格行结束符的副本：

`mac2unix {{-n|--newfile}} {{path/to/file}} {{path/to/new_file}}`

- 显示文件信息：

`mac2unix {{-i|--info}} {{path/to/file}}`

- 保留/添加/删除字节顺序标记：

`mac2unix --{{keep-bom|add-bom|remove-bom}} {{path/to/file}}`