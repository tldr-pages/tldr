# expr

> 评估表达式和操作字符串。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/expr-invocation.html>.

- 获取特定字符串的长度：

`expr length "{{string}}"`

- 获取字符串的特定长度的子字符串：

`expr substr "{{string}}" {{from}} {{length}}`

- 匹配字符串中的特定子字符串与定位模式：

`expr match "{{string}}" '{{pattern}}'`

- 获取字符串中特定字符集的第一个字符位置：

`expr index "{{string}}" "{{chars}}"`

- 计算特定的数学表达式：

`expr {{expression1}} {{+|-|*|/|%}} {{expression2}}`

- 如果第一个表达式的值为非零且非空，则获取第一个表达式，否则获取第二个表达式：

`expr {{expression1}} \| {{expression2}}`

- 如果两个表达式的值均为非零且非空，则获取第一个表达式，否则获取零：

`expr {{expression1}} \& {{expression2}}`
