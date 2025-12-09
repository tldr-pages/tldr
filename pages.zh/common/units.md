# units

> 提供两个度量单位之间的转换。
> 更多信息：<https://www.gnu.org/software/units/manual/units.html>.

- 以交互模式运行：

`units`

- 在交互模式下列出包含特定字符串的所有单位：

`search {{字符串}}`

- 显示两个简单单位之间的转换：

`units {{quarts(夸脱)}} {{tablespoons(大汤匙)}}`

- 单位与数量之间的转换：

`units "{{15 pounds(磅)}}" {{kilograms(公斤)}}`

- 显示两个复合单位之间的转换：

`units "{{meters(米) / second(秒)}}" "{{inches(英寸) / hour(小时)}}"`

- 显示具有不同维度的单位之间的转换：

`units "{{acres(英亩)}}" "{{ft^2(平方英尺)}}"`

- 显示字节乘数的转换：

`units "{{15 megabytes(兆字节)}}" {{bytes(字节)}}`
