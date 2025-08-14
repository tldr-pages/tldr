# complete

> Get and set argument autocompletion to shell commands.
> The specified completions will be invoked when `<Tab>` is pressed in Bash.
> See also: `compgen`, `compopt`.
> More information: <https://www.gnu.org/software/bash/manual/html_node/Programmable-Completion-Builtins.html#index-complete>.

- Set arguments of a command to autocomplete through a function (completion response is sent in `COMPREPLY` variable):

`complete -F {{function}} {{command}}`

- Set arguments of a command to autocomplete through another command (`$1` is the command, `$2` is the argument the cursor is on, and `$3` is the argument preceding the cursor):

`complete -C {{autocomplete_command}} {{command}}`

- Set arguments of a command to autocomplete to shell builtins:

`complete -A builtin {{command}}`

- Apply autocompletion without appending a space to the completed word:

`complete -o nospace -F {{function}} {{command}}`

- List all loaded complete specifications:

`complete -p`

- List loaded complete specifications for  a command:

`complete -p {{command}}`
