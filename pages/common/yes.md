# yes

> Output something repeatedly.
> This command is commonly used to answer yes to every prompt by install commands (such as apt-get).
> More information: <https://www.gnu.org/software/coreutils/yes>.

- Repeatedly output "message":

`yes {{message}}`

- Repeatedly output "y":

`yes`

- Accept everything prompted by the `apt-get` command:

`yes | sudo apt-get install {{program}}`

- Repeatedly output a newline to always accept the default option of a prompt:

`yes ''`
