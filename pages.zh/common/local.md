# local

> 声明局部变量并赋予它们属性。
> 参见：`declare`。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-local>。

- 声明一个具有指定值的字符串变量：

`local {{variable}}="{{value}}"`

- 声明一个具有指定值的整数变量：

`local -i {{variable}}="{{value}}"`

- 声明一个具有指定值的数组变量：

`local {{variable}}=({{item_a item_b item_c}})`

- 声明一个具有指定值的关联数组变量：

`local -A {{variable}}=({{[key_a]=item_a [key_b]=item_b [key_c]=item_c}})`

- 声明一个只读变量并赋予指定值：

`local -r {{variable}}="{{value}}"`

- 显示帮助：

`local --help`
