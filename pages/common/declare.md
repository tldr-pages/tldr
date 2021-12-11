# declare

> Declare variables and give them attributes.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#Bash-Builtins>.

- Declare a string variable:

`declare {{variable}}="{{value}}"`

- Declare an integer variable:

`declare -i {{variable}}="{{value}}"`

- Declare an array variable:

`declare {{variable}}=({{item_a item_b item_c}})`

- Declare an associative array variable:

`declare -A {{variable}}=({{[key_a]=item_a [key_b]=item_b [key_c]=item_c}})`

- Declare a readonly string variable:

`declare -r {{variable}}="{{value}}"`

- Declare a global variable even within function:

`declare -g {{variable}}="{{value}}"`
