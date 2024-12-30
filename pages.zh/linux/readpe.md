# readpe

> 显示有关PE文件的信息。
> 更多信息：<https://manned.org/readpe>。

- 显示PE文件的所有信息：

`readpe {{路径/到/可执行文件}}`

- 显示PE文件中存在的所有头信息：

`readpe --all-headers {{路径/到/可执行文件}}`

- 显示PE文件中存在的所有节：

`readpe --all-sections {{路径/到/可执行文件}}`

- 显示PE文件中的特定头信息：

`readpe --header {{dos|coff|optional}} {{路径/到/可执行文件}}`

- 列出所有导入的函数：

`readpe --imports {{路径/到/可执行文件}}`

- 列出所有导出的函数：

`readpe --exports {{路径/到/可执行文件}}`