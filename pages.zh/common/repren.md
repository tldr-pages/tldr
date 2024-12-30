# repren

> 多模式字符串替换和文件重命名工具。
> 更多信息：<https://github.com/jlevy/repren>。

- 进行一次干运行，将一个PNG目录中的文件名进行字面字符串替换：

`repren --dry-run --rename --literal --from '{{find_string}}' --to '{{replacement_string}}' {{*.png}}`

- 进行一次干运行，将一个JPEG目录中的文件名进行正则表达式替换：

`repren --rename --dry-run --from '{{regular_expression}}' --to '{{replacement_string}}' {{*.jpg}} {{*.jpeg}}`

- 在一个CSV文件目录的内容上进行查找和替换：

`repren --from '{{([0-9]+) example_string}}' --to '{{replacement_string \1}}' {{*.csv}}`

- 同时进行查找和替换以及重命名操作，使用模式文件：

`repren --patterns {{path/to/patfile.ext}} --full {{*.txt}}`

- 进行不区分大小写的重命名：

`repren --rename --insensitive --patterns {{path/to/patfile.ext}} *`