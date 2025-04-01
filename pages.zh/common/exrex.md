# exrex

> 为正则表达式生成所有或随机匹配字符串。
> 也可以简化正则表达式。
> 更多信息：<https://github.com/asciimoo/exrex>。

- 生成所有可能匹配正则表达式的字符串：

`exrex '{{regular_expression}}'`

- 生成一个随机匹配正则表达式的字符串：

`exrex --random '{{regular_expression}}'`

- 生成最多 100 个匹配正则表达式的字符串：

`exrex --max-number {{100}} '{{regular_expression}}'`

- 生成所有可能匹配正则表达式的字符串，使用自定义分隔符连接：

`exrex --delimiter "{{, }}" '{{regular_expression}}'`

- 打印所有可能匹配正则表达式的字符串的数量：

`exrex --count '{{regular_expression}}'`

- 简化正则表达式：

`exrex --simplify '{{ab|ac}}'`

- 打印眼睛：

`exrex '{{[oO0](_)[oO0]}}'`

- 打印一艘船：

`exrex '{{( {20}(\| *\\|-{22}|\|)|\.={50}| ( ){0,5}\\\.| {12}~{39})}}'`