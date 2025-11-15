# man

> 展示手册分页 (manual page).
> 更多信息：<https://manned.org/man>.

- 展示一条命令的使用手册分页:

`man {{command}}`

- 在浏览器中打开一条命令的使用手册分页 (`BROWSER` 环境变量可以替换 `=browser_name`):

`man {{[-Hbrowser_name|--html=browser_name]}} {{command}}`

- 从第七章节展示一条命令的使用手册分页:

`man {{7}} {{command}}`

- 列表展示一条命令的所有可用章节:

`man {{[-f|--whatis]}} {{command}}`

- 展示搜索手册分页的路径:

`man {{[-w|--path]}}`

- 展示使用手册分页的位置, 而不是手册分页本身:

`man {{[-w|--where]}} {{command}}`

- 使用特定的语言来展示使用手册分页:

`man {{[-L|--locale]}} {{locale}} {{command}}`

- 搜索包含搜索字符串的手册页:

`man {{[-k|--apropos]}} "{{search_string}}"`
