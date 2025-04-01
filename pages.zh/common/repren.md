# repren

> 多模式字符串替换和文件重命名工具。
> 更多信息：<https://github.com/jlevy/repren>。

- 对 PNG 文件目录进行干运行，使用字面字符串替换：

`repren --dry-run --rename --literal --from '{{find_string}}' --to '{{replacement_string}}' {{*.png}}`

- 对 JPEG 文件目录进行干运行，使用正则表达式：

`repren --rename --dry-run --from '{{regular_expression}}' --to '{{replacement_string}}' {{*.jpg}} {{*.jpeg}}`

- 对 CSV 文件目录内容进行查找和替换：

`repren --from '{{([0-9]+) example_string}}' --to '{{replacement_string \1}}' {{*.csv}}`

- 同时进行查找替换和重命名操作，使用模式文件：

`repren --patterns {{path/to/patfile.ext}} --full {{*.txt}}`

- 进行不区分大小写的重命名：

`repren --rename --insensitive --patterns {{path/to/patfile.ext}} *`