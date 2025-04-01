# readpe

> 显示 PE 文件的信息。
> 更多信息：<https://manned.org/readpe>.

- 显示 PE 文件的所有信息：

`readpe {{path/to/executable}}`

- 显示 PE 文件中的所有头部信息：

`readpe --all-headers {{path/to/executable}}`

- 显示 PE 文件中的所有节：

`readpe --all-sections {{path/to/executable}}`

- 显示 PE 文件中的特定头部信息：

`readpe --header {{dos|coff|optional}} {{path/to/executable}}`

- 列出所有导入的函数：

`readpe --imports {{path/to/executable}}`

- 列出所有导出的函数：

`readpe --exports {{path/to/executable}}`
