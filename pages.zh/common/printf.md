# printf

> 格式化并打印文本。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/printf-invocation.html>.

- 打印文本消息：

`printf "{{%s\n}}" "{{文本}}"`

- 以粗体蓝色打印整数：

`printf "{{\e[1;34m%.3d\e[0m\n}}" {{42}}`

- 打印带有 Unicode 欧元符号的浮点数：

`printf "{{\u20AC %.2f\n}}" {{123.4}}`

- 打印由环境变量组成的文本消息：

`printf "{{var1: %s\tvar2: %s\n}}" "{{$VAR1}}" "{{$VAR2}}"`

- 将格式化消息存储在变量中（不适用于 Zsh）：

`printf -v {{变量名}} {{"这是 %s = %d年\n" "今" 2016}}`

- 打印十六进制、八进制和科学计数法数字：

`printf "{{hex=%x octal=%o scientific=%e}}" 0x{{FF}} 0{{377}} {{100000}}`
