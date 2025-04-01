# declare

> 声明变量并赋予它们属性。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-declare>.

- 声明一个具有指定值的字符串变量：

`declare {{variable}}="{{value}}"`

- 声明一个具有指定值的整数变量：

`declare -i {{variable}}="{{value}}"`

- 声明一个具有指定值的数组变量：

`declare -a {{variable}}=({{item_a item_b item_c}})`

- 声明一个具有指定值的关联数组变量：

`declare -A {{variable}}=({{[key_a]=item_a [key_b]=item_b [key_c]=item_c}})`

- 声明一个具有指定值的只读字符串变量：

`declare -r {{variable}}="{{value}}"`

- 在函数内部声明一个具有指定值的全局变量：

`declare -g {{variable}}="{{value}}"`

- 打印函数定义：

`declare -f {{function_name}}`