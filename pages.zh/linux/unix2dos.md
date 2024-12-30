# unix2dos

> 将 Unix 风格的行结束符转换为 DOS 风格。
> 将 LF 替换为 CRLF。
> 另见 `unix2mac`、`dos2unix` 和 `mac2unix`。
> 更多信息：<https://manned.org/unix2dos>。

- 更改文件的行结束符：

`unix2dos {{path/to/file}}`

- 创建一个带有 DOS 风格行结束符的副本：

`unix2dos {{-n|--newfile}} {{path/to/file}} {{path/to/new_file}}`

- 显示文件信息：

`unix2dos {{-i|--info}} {{path/to/file}}`

- 保持/添加/移除字节顺序标记（BOM）：

`unix2dos --{{keep-bom|add-bom|remove-bom}} {{path/to/file}}`