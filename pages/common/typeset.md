# typeset

> Declare variables and give them attributes.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#Bash-Builtins>.

- Declare a string variable:

`typeset {{variable}}="{{value}}"`

- Declare an integer variable:

`typeset -i {{variable}}="{{value}}"`

- Declare an readonly string variable:

`typeset -r {{variable}}="{{value}}"`

- Declare an readonly integer variable:

`typeset -ir {{variable}}="{{value}}"`
