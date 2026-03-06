# float

> Declare floating point variable(s).
> Equivalent to `typeset -E` except that options irrelevant to floating point numbers are not permitted.
> See also: `typeset`, `declare`.
> More information: <https://manned.org/zshbuiltins>.

- Declare a floating point variable:

`float {{variable_name}}`

- Declare a floating point variable while assigning its value:

`float {{variable_name}}={{value}}`

- Declare multiple floating point variables:

`float {{var1=value1 var2=value2 ...}}`

- Display defined variables:

`float`
