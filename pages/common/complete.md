# complete

> Provides argument autocompletion to shell commands.

- Apply an autocomplete function to a command:

`complete -F {{function}} {{command}}`

- Apply an autocomplete command to a command:

`complete -C {{autocomplete_command}} {{command}}`

- Apply autocompletion without appending a space to the completed word:

`complete -o nospace -F {{function}} {{command}}`
