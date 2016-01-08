# php

> PHP Command Line Interface 'CLI'.

- Parse and execute a file:

`php {{file}}`

- Check syntax (lint):

`php -l {{file}}`

- Run PHP interactively:

`php -a`

- Run PHP code. Notes: a) Don't use <? ?> tags; b) Escape double quotes with backslash:

`php -r "{{code}}"`

- Start a PHP built-in web server in the current directory:

`php -S {{host:port}}`
