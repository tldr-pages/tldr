# local

> Declare local variables and give them attributes.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#Bash-Builtins>.

- Declare a string variable:

`local {{variable}}="{{value}}"`

- Declare an integer variable:

`local -i {{variable}}="{{value}}"`

- Declare an array variable:

`local {{variable}}=({{item_a item_b item_c}})`

- Declare an associative array variable:

`local -A {{variable}}=({{[key_a]=item_a [key_b]=item_b [key_c]=item_c}})`

- Declare a readonly variable:

`local -r {{variable}}="{{value}}"`
