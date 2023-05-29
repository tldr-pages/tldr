# arithmetic

> 测试见到你的算术问题。
> 更多信息：<https://manpages.debian.org/latest/bsdgames/arithmetic.6.en.html>.

- 开始算术测试：

`arithmetic`

- 指定一个或多个算术运算符来设计问题：

`arithmetic -o {{+|-|x|/}}`

- 指定范围。加法和乘法问题限定 0 到指定范围之间的数字，包含上区间。减法和除法问题限制结果和运算数字必须在 0 到指定范围之间：

`arithmetic -r {{7}}`
