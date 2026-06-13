# php

> PHP command-line interface.
> More information: <https://www.php.net/manual/en/features.commandline.options.php>.

- Parse and execute a PHP script:

`php {{path/to/file}}`

- Check syntax on (i.e. [l]int) a PHP script:

`php {{[-l|--syntax-check]}} {{path/to/file}}`

- Run PHP inter[a]ctively:

`php {{[-a|--interactive]}}`

- Run PHP code (Notes: Don't use `<? ?>` tags; escape double quotes with backslash):

`php {{[-r|--run]}} "{{code}}"`

- Start a PHP built-in web server in the current directory:

`php {{[-S|--server]}} {{host}}:{{port}}`

- List installed PHP extensions:

`php {{[-m|--modules]}}`

- Display information about the current PHP configuration:

`php {{[-i|--info]}}`

- Display information about a specific function:

`php {{[--rf|--rfunction]}} {{function_name}}`
