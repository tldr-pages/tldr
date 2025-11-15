# compgen

> Bash built-in command for generating possible completion matches in Bash.
> Usually used within custom completion functions.
> See also: `complete`, `compopt`.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#index-compgen>.

- List all shell built-ins, aliases, functions and executables that you could run:

`compgen -c`

- List all commands that you could run that start with a specified string and save results to `COMPREPLY`:

`compgen -V COMPREPLY -c {{str}}`

- Match against a wordlist:

`compgen -W "{{apple orange banana}}" {{a}}`

- List all aliases:

`compgen -a`

- List all functions that you could run:

`compgen -A function`

- Show shell reserved keywords:

`compgen -k`

- See all available commands/aliases starting with `ls`:

`compgen -ac {{ls}}`

- List all users on the system:

`compgen -u`
