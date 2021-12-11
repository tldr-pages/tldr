# typeset

> Declare variables and give them attributes.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#Bash-Builtins>.

- Declare a string variable:

`typeset {{variable}}="{{value}}"`

- Declare an integer variable:

`typeset -i {{variable}}="{{value}}"`

- Declare a readonly string variable:

`typeset -r {{variable}}="{{value}}"`

- Declare a readonly integer variable:

`typeset -ir {{variable}}="{{value}}"`
