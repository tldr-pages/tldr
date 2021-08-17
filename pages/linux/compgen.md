# compgen

> A built-in command for auto-completion in Bash, which is called on pressing TAB key twice.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#index-compgen>.

- List all commands that you could run:

`compgen -c`

- List all aliases:

`compgen -a`

- List all functions that you could run:

`compgen -A function`

- Show shell reserved keywords:

`compgen -k`

- See all available commands/aliases starting with 'ls':

`compgen -ac {{ls}}`
