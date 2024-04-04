# php

> PHP command-line interface.
> More information: <https://php.net>.

- Parse and execute a PHP script:

`php {{path/to/file}}`

- Check syntax on (i.e. lint) a PHP script:

`php -l {{path/to/file}}`

- Run PHP interactively:

`php -a`

- Run PHP code (Notes: Don't use <? ?> tags; escape double quotes with backslash):

`php -r "{{code}}"`

- Start a PHP built-in web server in the current directory:

`php -S {{host:port}}`

- List installed PHP extensions:

`php -m`

- Display information about the current PHP configuration:

`php -i`

- Display information about a specific function:

`php --rf {{function_name}}`
