# dc

> 一个任意精度计算器。使用逆波兰表示法（RPN）。
> 另请参见：`bc`，`qalc`。
> 更多信息：<https://www.gnu.org/software/bc/manual/dc-1.05/html_mono/dc.html>。

- 开始一个交互会话：

`dc`

- 执行一个脚本：

`dc {{path/to/script.dc}}`

- 以指定的精度计算一个表达式：

`dc --expression='{{10}} k {{5 3 /}} p'`

- 计算4乘5（4 5 *），减去17（17 -），并[p]rint输出：

`dc --expression='4 5 * 17 - p'`

- 将小数位数指定为7（7 k），计算5除以-3（5 _3 /）并[p]rint：

`dc --expression='7 k 5 _3 / p'`

- 计算黄金比例，phi：将小数位数设为100（100 k），5的平方根（5 v）加1（1 +），除以2（2 /），并[p]rint结果：

`dc --expression='100 k 5 v 1 + 2 / p'`