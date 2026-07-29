# local

> 声明局部变量并为其赋予属性。
> 另请参阅：`declare`、`export`。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-local>。

- 声明具有指定值的字符串变量：

`local {{变量}}="{{值}}"`

- 声明具有指定值的整数变量：

`local -i {{变量}}="{{值}}"`

- 声明具有指定值的数组变量：

`local {{变量}}=({{元素_a 元素_b 元素_c}})`

- 声明具有指定值的关联数组变量：

`local -A {{变量}}=({{[键_a]=元素_a [键_b]=元素_b [键_c]=元素_c}})`

- 声明具有指定值的只读变量：

`local -r {{变量}}="{{值}}"`

- 显示帮助信息：

`local --help`
