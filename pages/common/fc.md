# fc

> Open the most recent command for editing and then run it.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#index-fc>.

- Open the last command in the default system editor and run it after editing:

`fc`

- Specify an editor to open with:

`fc -e '{{emacs}}'`

- List recent commands from history:

`fc -l`

- List recent commands in reverse order:

`fc -l -r`

- Edit and run a command from history:

`fc {{number}}`

- Edit commands in a given interval and run them:

`fc '{{416}}' '{{420}}'`

- Display help:

`fc --help`
