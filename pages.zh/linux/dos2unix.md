# dos2unix

> 将 DOS 风格的行结束符转换为 Unix 风格。
> 将 CRLF 替换为 LF。
> 另见 `unix2dos`、`unix2mac` 和 `mac2unix`。
> 更多信息：<https://manned.org/dos2unix>。

- 更改文件的行结束符：

`dos2unix {{path/to/file}}`

- 创建一个带有 Unix 风格行结束符的副本：

`dos2unix {{-n|--newfile}} {{path/to/file}} {{path/to/new_file}}`

- 显示文件信息：

`dos2unix {{-i|--info}} {{path/to/file}}`

- 保留/添加/移除字节顺序标记：

`dos2unix --{{keep-bom|add-bom|remove-bom}} {{path/to/file}}`