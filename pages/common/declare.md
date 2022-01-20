# declare

> Declare variables and give them attributes.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#Bash-Builtins>.

- Declare a string variable with the specified value:

`declare {{variable}}="{{value}}"`

- Declare an integer variable with the specified value:

`declare -i {{variable}}="{{value}}"`

- Declare an array variable with the specified value:

`declare -a {{variable}}=({{item_a item_b item_c}})`

- Declare an associative array variable with the specified value:

`declare -A {{variable}}=({{[key_a]=item_a [key_b]=item_b [key_c]=item_c}})`

- Declare a readonly string variable with the specified value:

`declare -r {{variable}}="{{value}}"`

- Declare a global variable within a function with the specified value:

`declare -g {{variable}}="{{value}}"`
