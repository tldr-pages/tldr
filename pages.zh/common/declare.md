# 声明

> 声明变量并赋予它们属性。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-declare>。

- 声明一个字符串变量并赋予指定值：

`declare {{variable}}="{{value}}"`

- 声明一个整数变量并赋予指定值：

`declare -i {{variable}}="{{value}}"`

- 声明一个数组变量并赋予指定值：

`declare -a {{variable}}=({{item_a item_b item_c}})`

- 声明一个关联数组变量并赋予指定值：

`declare -A {{variable}}=({{[key_a]=item_a [key_b]=item_b [key_c]=item_c}})`

- 声明一个只读字符串变量并赋予指定值：

`declare -r {{variable}}="{{value}}"`

- 在函数内声明一个全局变量并赋予指定值：

`declare -g {{variable}}="{{value}}"`

- 打印函数定义：

`declare -f {{function_name}}`