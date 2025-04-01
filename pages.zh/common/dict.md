# dict

> 使用 DICT 协议的命令行字典。
> 更多信息：<https://github.com/cheusov/dictd>.

- 列出可用的数据库：

`dict -D`

- 获取关于某个数据库的信息：

`dict -i {{database_name}}`

- 在特定数据库中查找单词：

`dict -d {{database_name}} {{word}}`

- 在所有可用数据库中查找单词：

`dict {{word}}`

- 显示关于 DICT 服务器的信息：

`dict -I`