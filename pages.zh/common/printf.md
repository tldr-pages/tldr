# printf

> 格式化并打印文本。
> 更多信息：<https://www.gnu.org/software/coreutils/printf>。

- 打印文本消息：

`printf "{{%s\n}}" "{{你好，世界}}"`

- 用粗体蓝色打印一个整数：

`printf "{{\e[1;34m%.3d\e[0m\n}}" {{42}}`

- 打印带有Unicode欧元符号的浮点数：

`printf "{{\u20AC %.2f\n}}" {{123.4}}`

- 打印由环境变量组成的文本消息：

`printf "{{var1: %s\tvar2: %s\n}}" "{{$VAR1}}" "{{$VAR2}}"`

- 将格式化消息存储在变量中（在Zsh中不起作用）：

`printf -v {{myvar}} {{"这就是 %s = %d\n" "一年" 2016}}`

- 打印十六进制、八进制和科学计数法数字：

`printf "{{hex=%x octal=%o scientific=%e}}" 0x{{FF}} 0{{377}} {{100000}}`