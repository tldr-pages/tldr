# typeset

> Declare variables and give them attributes.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#Bash-Builtins>.

- Declare a string variable:

`typeset {{variable}}="{{value}}"`

- Declare an integer variable:

`typeset -i {{variable}}="{{value}}"`

- Declare an array variable:

`typeset {{variable}}=({{item_a item_b item_c}})`

- Declare an associative array variable:

`typeset -A {{variable}}=({{[key_a]=item_a [key_b]=item_b [key_c]=item_c}})`

- Declare a readonly variable:

`typeset -r {{variable}}="{{value}}"`

- Declare a global variable even within function:

`typeset -g {{variable}}="{{value}}"`
