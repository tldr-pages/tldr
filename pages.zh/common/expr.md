# expr

> 评估表达式并处理字符串。
> 更多信息：<https://www.gnu.org/software/coreutils/expr>。

- 获取特定字符串的长度：

`expr length "{{string}}"`

- 获取特定长度的字符串子串：

`expr substr "{{string}}" {{from}} {{length}}`

- 将特定子串与固定模式进行匹配：

`expr match "{{string}}" '{{pattern}}'`

- 获取字符串中特定字符集合的第一个字符位置：

`expr index "{{string}}" "{{chars}}"`

- 计算特定的数学表达式：

`expr {{expression1}} {{+|-|*|/|%}} {{expression2}}`

- 如果第一个表达式的值非零且不为空，则获取第一个表达式，否则获取第二个表达式：

`expr {{expression1}} \| {{expression2}}`

- 如果两个表达式都非零且不为空，则获取第一个表达式，否则获取零：

`expr {{expression1}} \& {{expression2}}`