# float

> Declare floating point variable(s).
> Equivalent to `typeset -E`.
> More information: <https://manned.org/zshbuiltins>.

- Declare a floating point variable:

`float {{variable_name}}`

- Declare a floating point variable while assigning its value:

`float {{variable_name}}={{value}}`

- Declare multiple floating point variables:

`float {{var1}} {{var2}} {{var3}}`

- Display defined variables:

`float`

- Specify the number of significant digits to display:

`float -E {{number_of_digits}} {{variable_name}}`
