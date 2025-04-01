# let

> 在 shell 中计算算术表达式。
> 支持变量、运算符和条件表达式。
> 更多信息：<https://manned.org/let>.

- 计算简单的算术表达式：

`let "{{result = a + b}}"`

- 在表达式中使用后缀自增和赋值：

`let "{{x++}}"`

- 在表达式中使用条件运算符：

`let "{{result = (x > 10) ? x : 0}}"`

- 显示帮助：

`let --help`