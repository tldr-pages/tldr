# function

> Define a function.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#Shell-Functions>.

- Define a function with the specified name:

`function {{func_name}} { {{echo "Function contents here"}}; }`

- Run a function named `func_name`:

`func_name`

- Define a function without the `function` keyword:

`{{func_name}}() { {{echo "Function contents here"}}; }`

- Display help:

`help function`
