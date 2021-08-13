# compgen

> A built-in command for auto-completion in bash, which is called on pressing TAB key twice.
> More information: <https://www.cyberciti.biz/open-source/command-line-hacks/compgen-linux-command/>.

- List all commands that you could run:

`compgen -c`

- List all aliases:

`compgen -a`

- List all functions that you could run:

`compgen -A function`

- Show shell reserved key words:

`compgen -k`

- See all available commands/aliases starting with 'ls':

`compgen -ac {{ls}}`
