# csvgrep

> 使用字符串和模式匹配过滤CSV行。
> 包含在csvkit中。
> 更多信息：<https://csvkit.readthedocs.io/en/latest/scripts/csvgrep.html>。

- 查找第一列中包含某个字符串的行：

`csvgrep -c {{1}} -m {{string_to_match}} {{data.csv}}`

- 查找第三列或第四列匹配某个正则表达式的行：

`csvgrep -c {{3,4}} -r {{regular_expression}} {{data.csv}}`

- 查找“name”列中不包含字符串“John Doe”的行：

`csvgrep -i -c {{name}} -m "{{John Doe}}" {{data.csv}}`