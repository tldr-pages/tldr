# vhs

> 从磁带文件生成终端 GIF。
> 更多信息：<https://github.com/charmbracelet/vhs>。

- 创建一个磁带文件（使用编辑器在磁带文件中添加命令）：

`vhs new {{path/to/file.tape}}`

- 记录输入到磁带文件（完成后，退出 shell 以创建磁带）：

`vhs record > {{path/to/file.tape}}`

- 使用特定的 shell 记录输入到磁带文件：

`vhs record --shell {{shell}} > {{path/to/file.tape}}`

- 验证磁带文件的语法：

`vhs validate {{path/to/file.tape}}`

- 从磁带文件创建 GIF：

`vhs < {{path/to/file.tape}}`

- 将 GIF 发布到 <https://vhs.charm.sh> 并获取可分享的 URL：

`vhs publish {{path/to/file.gif}}`
