# csvgrep

> 通过字符串和模式匹配筛选 CSV 行。
> 包含在 csvkit 中。
> 更多信息：<https://csvkit.readthedocs.io/en/latest/scripts/csvgrep.html>.

- 找出第 1 列包含特定字符串的行：

`csvgrep -c {{1}} -m {{string_to_match}} {{data.csv}}`

- 找出第 3 列或第 4 列匹配特定正则表达式的行：

`csvgrep -c {{3,4}} -r {{regular_expression}} {{data.csv}}`

- 找出“name”列不包含字符串“John Doe”的行：

`csvgrep -i -c {{name}} -m "{{John Doe}}" {{data.csv}}`