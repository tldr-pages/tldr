# let

> 在 shell 中计算算术表达式。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-let>。

- 计算简单的算术表达式：

`let "{{结果 = a + b}}"`

- 在表达式中使用自增和赋值：

`let "{{x++}}"`

- 在表达式中使用条件运算符：

`let "{{结果 = (x > 10) ? x : 0}}"`

- 显示帮助信息：

`let --help`
