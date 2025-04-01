# ffe

> 从平面数据库文件中提取字段并写入另一种格式。
> 需要一个配置文件来解释输入并格式化输出。
> 更多信息：<https://ff-extractor.sourceforge.net/ffe.html>.

- 使用指定的数据配置显示所有输入数据：

`ffe --configuration={{path/to/config.ffe}} {{path/to/input}}`

- 将输入文件转换为新格式的输出文件：

`ffe --output={{path/to/output}} -c {{path/to/config.ffe}} {{path/to/input}}`

- 从 `~/.fferc` 配置文件中的定义选择输入结构和打印格式：

`ffe --structure={{structure}} --print={{format}} {{path/to/input}}`

- 仅写入选定的字段：

`ffe --field-list="{{FirstName,LastName,Age}}" -c {{path/to/config.ffe}} {{path/to/input}}`

- 仅写入与表达式匹配的记录：

`ffe -e "{{LastName=Smith}}" -c {{path/to/config.ffe}} {{path/to/input}}`

- 显示帮助：

`ffe --help`
