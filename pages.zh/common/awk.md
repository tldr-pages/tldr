# awk

> 一种用于处理文件的多功能编程语言。
> 更多信息：<https://github.com/onetrueawk/awk>。

- 打印以空格分隔的文件中的第五列（即字段）：

`awk '{print $5}' {{path/to/file}}`

- 打印包含“foo”的行的第二列，文件以空格分隔：

`awk '/{{foo}}/ {print $2}' {{path/to/file}}`

- 打印文件中每行的最后一列，以逗号（而不是空格）作为字段分隔符：

`awk -F ',' '{print $NF}' {{path/to/file}}`

- 对文件的第一列值求和并打印总和：

`awk '{s+=$1} END {print s}' {{path/to/file}}`

- 从第一行开始打印每第三行：

`awk 'NR%3==1' {{path/to/file}}`

- 根据条件打印不同的值：

`awk '{if ($1 == "foo") print "完全匹配 foo"; else if ($1 ~ "bar") print "部分匹配 bar"; else print "Baz"}' {{path/to/file}}`

- 打印第十列值在最小值和最大值之间的所有行：

`awk '($10 >= {{min_value}} && $10 <= {{max_value}})'`

- 打印 UID >= 1000 的用户表，带有标题和格式化输出，使用冒号作为分隔符（`%-20s` 意思是：20个左对齐的字符串字符，`%6s` 意思是：6个右对齐的字符串字符）：

`awk 'BEGIN {FS=":";printf "%-20s %6s %25s\n", "姓名", "UID", "Shell"} $4 >= 1000 {printf "%-20s %6d %25s\n", $1, $4, $7}' /etc/passwd`